# Mermaid Js Diagram for E
```mermaid
graph RL;
conract_emp.sql -->EMPLOYEE;
DEPT -->conract_emp.sql:::sqlClass;
CONTRACT_EMP_STG -->conract_emp.sql:::sqlClass;
BUS_UNIT -->conract_emp.sql:::sqlClass;
perm_emp.sql -->EMPLOYEE;
DEPT -->perm_emp.sql:::sqlClass;
PERM_EMP_STG -->perm_emp.sql:::sqlClass;
BUS_UNIT -->perm_emp.sql:::sqlClass;
dept.sql -->DEPT;
COMPENSATION -->dept.sql:::sqlClass;
DEPT_STG -->dept.sql:::sqlClass;
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
[Mermaid JS API](https://kroki.io/mermaid/svg/eNqFkV0LgjAUhu_9FULXdhm0QVA6IsgPdF10NcxmCVOX0_-fi05u0ceNwtnzvucZu3S5vLrpHjtF23R50TNey7m6CdfzViRM9vGREOwEJKF68gYhhMavL3KlsOPHEU3XPmVjjGV0-4_fHDJ2iHZ_eyXv6t9WJmFFE5KGps5X0HT5Cp257EFCr9ZXDhMSZWu6iyM9BcKKaRQEPgKnQbGhqV7dIDNpQdwkrYotiX-eF20teaPyvmobWGPK21eZXs9OWZUX3kLTuP2hALnnkW2gfwEvXRi5ZSUEmpXLBb4Dn9TS_g==)