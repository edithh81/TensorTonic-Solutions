from typing import List, Tuple

type_map = {
        "str": str,
        "int": int,
        "float": float
}
def build_checks(col_schema):
    col = col_schema["column"]
    type_ = type_map[col_schema["type"]]

    checks = [
        lambda v: None if (col_schema.get("nullable", True) or v is not None)
        else f"{col}: null",

        lambda v: None if (
        v is None or
        (col_schema["type"] == "float" and (type(v) is int \
                                            or type(v) is float ) or
        type(v) is type_
        )) \
        else f"{col}: expected {col_schema['type']}, got {type(v).__name__}"
    ]

    if "min" in col_schema:
        checks.append(lambda v, m=col_schema["min"]:
                      None if (v is None or v >= m) else f"{col}: out of range")

    if "max" in col_schema:
        checks.append(lambda v, m=col_schema["max"]:
                      None if (v is None or v <= m) else f"{col}: out of range")

    return checks

def validate_row(row, schema):
    # errors = ["type: "]
    errors = []
    
    for col_schema in schema:
        col = col_schema['column']
        if col in row:
            val = row.get(col)
            for check in build_checks(col_schema):
                err = check(val)
                if err:
                    errors.append(err)
                    break
        else:
            errors.append(f"{col}: missing")
    return errors
        
def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    # Write code here
    # return as [(idx, True/False, [<list error if exists>])]
    val_res = []
    for i, rec in enumerate(records):
        # one rec id dict
        schema_val = validate_row(rec, schema)
        val_res.append((i, False if len(schema_val) else True , schema_val))

    return val_res
        
        
    