// Copyright 2021-present StarRocks, Inc. All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include "column/array_column.h"
#include "column/column_helper.h"
#include "column/const_column.h"
#include "column/type_traits.h"
#include "column/vectorized_fwd.h"
#include "gutil/casts.h"
#include "util/slice.h"

namespace starrocks {
class FunctionContext;
}
namespace starrocks {

class FunctionHelper {
public:
    /**
     * if ptr is NullableColumn, return data column
     * else return ptr
     * @param ptr 
     */
    static inline const ColumnPtr& get_data_column_of_nullable(const ColumnPtr& ptr) {
        if (ptr->is_nullable()) {
            return down_cast<NullableColumn*>(ptr.get())->data_column();
        }
        return ptr;
    }

    template <typename ToPtrType>
    static ToPtrType unwrap_if_nullable(const Column* col, int row_num) {
        if (col->is_nullable()) {
            if (col->is_null(row_num)) {
                return nullptr;
            }
            auto null_col = dynamic_cast<const NullableColumn*>(col);
            return dynamic_cast<ToPtrType>(null_col->data_column().get());
        }
        return dynamic_cast<ToPtrType>(col);
    }

    template <typename ToPtrType>
    static ToPtrType unwrap_if_const(const Column* col) {
        if (col->is_constant()) {
            auto const_col = dynamic_cast<const ConstColumn*>(col);
            return dynamic_cast<ToPtrType>(const_col->data_column().get());
        }
        return dynamic_cast<ToPtrType>(col);
    }

    template <typename ToColumnType>
    static bool can_cast(const Column* col) {
        if (col->is_nullable()) {
            col = down_cast<const NullableColumn*>(col)->data_column().get();
        }
        if (col->is_constant()) {
            col = down_cast<const ConstColumn*>(col)->data_column().get();
        }
        return dynamic_cast<const ToColumnType*>(col) != nullptr;
    }

    template <typename ToPtrType, typename CppType>
    static bool get_data_of_column(const Column* col, size_t row_num, CppType& data) {
        col = unwrap_if_nullable<const Column*>(col, row_num);
        if (col == nullptr) {
            return false;
        }
        if (col->is_constant()) {
            auto const_col = dynamic_cast<const ConstColumn*>(col);
            if (const_col == nullptr) {
                return false;
            }
            const auto* column = dynamic_cast<const ToPtrType*>(const_col->data_column().get());
            data = column->get_data()[0];
            return true;
        }
        const auto* column = dynamic_cast<const ToPtrType*>(col);
        if (column == nullptr) {
            return false;
        }
        data = column->get_data()[row_num];
        return true;
    }

    static std::optional<DatumArray> get_data_of_array(const Column* col, size_t row_num) {
        const auto* data_column = FunctionHelper::unwrap_if_nullable<const ArrayColumn*>(col, row_num);
        if (data_column == nullptr) {
            return {};
        }
        return data_column->get(row_num).get_array();
    }

    /**
     * if ptr is ConstColumn, return data column
     * else return ptr
     * @param ptr 
     */
    static inline const ColumnPtr& get_data_column_of_const(const ColumnPtr& ptr) {
        if (ptr->is_constant()) {
            return down_cast<ConstColumn*>(ptr.get())->data_column();
        }
        return ptr;
    }

    /**
     * if v1 is NullableColumn and v2 is NullableColumn, union
     * if v1 is NullableColumn and v2 is not NullableColumn, return v1.nullColumn
     * if v1 is not NullableColumn and v2 is NullableColumn, return v2.nullColumn
     * if v1 is not NullableColumn and v2 is not NullableColumn, impossible
     * 
     * @param v1 
     * @param v2 
     */
    static NullColumnPtr union_nullable_column(const ColumnPtr& v1, const ColumnPtr& v2);

    static void union_produce_nullable_column(const ColumnPtr& v1, const ColumnPtr& v2,
                                              NullColumnPtr* produce_null_column);

    static void union_produce_nullable_column(const ColumnPtr& v1, NullColumnPtr* produce_null_column);

    static NullColumnPtr union_null_column(const NullColumnPtr& v1, const NullColumnPtr& v2);

    // merge a column and null_column and generate a column with null values.
    static ColumnPtr merge_column_and_null_column(ColumnPtr&& column, NullColumnPtr&& null_column);
};

#define DEFINE_VECTORIZED_FN(NAME) static StatusOr<ColumnPtr> NAME(FunctionContext* context, const Columns& columns)

#define DEFINE_VECTORIZED_FN_TEMPLATE(NAME) \
    template <LogicalType Type>             \
    static StatusOr<ColumnPtr> NAME(FunctionContext* context, const Columns& columns)

#define VECTORIZED_FN_CTX() context
#define VECTORIZED_FN_ARGS(IDX) columns[IDX]

#define RETURN_IF_COLUMNS_ONLY_NULL(COLUMNS) \
    do {                                     \
        for (auto& col : COLUMNS) {          \
            if (col->only_null()) {          \
                return col;                  \
            }                                \
        }                                    \
    } while (false)

} // namespace starrocks
