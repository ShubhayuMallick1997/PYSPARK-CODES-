
---

# 📂 7. Joins in PySpark

---

## 🔹 What are Joins in PySpark?

A **join** in PySpark combines rows from two or more DataFrames based on a related column (also called a **key**). It's commonly used to bring together data from multiple sources or tables.

PySpark supports **multiple types of joins**, similar to SQL.

---

## ✅ 1. Inner Join

An **inner join** returns only the rows that have matching keys in both DataFrames.

**Example:**

```python
df1.join(df2, on="id", how="inner").show()
```

Only rows with the same `id` in both `df1` and `df2` are returned.

---

## ✅ 2. Left Outer Join (or Left Join)

Returns all rows from the **left** DataFrame and matched rows from the right DataFrame. Non-matching rows will have `null` in the right-side columns.

**Example:**

```python
df1.join(df2, on="id", how="left").show()
```

---

## ✅ 3. Right Outer Join (or Right Join)

Returns all rows from the **right** DataFrame and matched rows from the left DataFrame.

**Example:**

```python
df1.join(df2, on="id", how="right").show()
```

---

## ✅ 4. Full Outer Join

Returns all rows from both DataFrames. When there's no match, the missing side will contain `null`.

**Example:**

```python
df1.join(df2, on="id", how="outer").show()
```

---

## ✅ 5. Left Semi Join

Returns rows from the **left** DataFrame **where a match exists** in the right DataFrame. It **does not return** columns from the right DataFrame.

**Example:**

```python
df1.join(df2, on="id", how="left_semi").show()
```

This is useful for filtering `df1` based on the presence of matching `id`s in `df2`.

---

## ✅ 6. Left Anti Join

Returns rows from the left DataFrame **where no match exists** in the right DataFrame.

**Example:**

```python
df1.join(df2, on="id", how="left_anti").show()
```

Often used to exclude overlapping records.

---

## ✅ 7. Cross Join (Cartesian Product)

Returns every combination of rows from both DataFrames. Can produce **very large** output and is rarely used in practice unless necessary.

**Example:**

```python
df1.crossJoin(df2).show()
```

> ⚠️ Avoid unless explicitly needed; use filters afterward to reduce result size.

---

## ✅ 8. Join on Multiple Columns

You can join on multiple keys by passing a list of column names.

**Example:**

```python
df1.join(df2, on=["id", "date"], how="inner").show()
```

---

## 🔍 Handling Column Name Conflicts

When both DataFrames have the same column names **not used for joining**, PySpark will append suffixes like `_1` and `_2`.

**To avoid ambiguity:**

* Rename columns before the join
* Use `select()` to include only needed columns

---

## ✅ 9. Broadcast Join

When joining a **small DataFrame with a large one**, use **broadcast joins** for performance optimization.

**Example:**

```python
from pyspark.sql.functions import broadcast

df1.join(broadcast(df2), on="id", how="inner").show()
```

> Broadcasting avoids expensive shuffles across the cluster by sending the small table to all worker nodes.

---

## ✅ Summary

| Join Type        | Description                              | Includes Right Columns? |
| ---------------- | ---------------------------------------- | ----------------------- |
| Inner Join       | Matches in both DataFrames               | ✅                       |
| Left Outer Join  | All from left, matched from right        | ✅                       |
| Right Outer Join | All from right, matched from left        | ✅                       |
| Full Outer Join  | All from both, null where unmatched      | ✅                       |
| Left Semi Join   | Only left rows where match exists        | ❌                       |
| Left Anti Join   | Only left rows where **no** match exists | ❌                       |
| Cross Join       | Cartesian product (all combinations)     | ✅                       |

---


