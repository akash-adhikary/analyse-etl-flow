# Mermaid Js Diagram for EMPLOYEE
```mermaid
graph RL;
conract_emp.sql -->EMPLOYEE;
DEPT -->conract_emp.sql:::sqlClass;
CONTRACT_EMP_STG -->conract_emp.sql:::sqlClass;
BUS_UNIT -->conract_emp.sql:::sqlClass;
perm_emp.sql -->EMPLOYEE;
BUS_UNIT -->perm_emp.sql:::sqlClass;
DEPT -->perm_emp.sql:::sqlClass;
PERM_EMP_STG -->perm_emp.sql:::sqlClass;
dept.sql -->DEPT;
DEPT_STG -->dept.sql:::sqlClass;
COMPENSATION -->dept.sql:::sqlClass;
bus_unit.sql -->BUS_UNIT;
BUS_UNIT_STG -->bus_unit.sql:::sqlClass;
GEO -->bus_unit.sql:::sqlClass;
compensation.sql -->COMPENSATION;
COMPENSATION_STG -->compensation.sql:::sqlClass;
geo.sql -->GEO;
GEO_STG -->geo.sql:::sqlClass;
classDef sqlClass fill:#f96;
```
# Mermaid Js Link (Open Via Browser)
[Mermaid JS API](https://kroki.io/mermaid/svg/eNqFkV8LgjAUxd_9FIOe7TFIITAbIagTnQ89DbNZgn-W0--fVre2yHrZ4N5zzv3d7dxl4oJi3zbytumyvGe8Fkt5rZBpbnAQ-eSAsW3scESnyofIsqzxdKtMSttwSUhjx6VstLGE7v_pt2nC0tD7myt4V3-nUhNUlWYH9FlBhONAZZ4VnrjoAWJKfWSDDbofbxJEOEwc6pFwVnQcJBua8pUNa70XhBmqUovYY_Kzn7e14I3M-rJtYIzKppO-f093aZFn3kLSOP2OAL5nSyeYrh0vEJRQUVaVtSjWK_sGq2XS_g==)