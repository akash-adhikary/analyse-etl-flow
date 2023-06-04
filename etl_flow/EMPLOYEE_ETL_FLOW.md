# Mermaid Js Diagram for EMPLOYEE
```mermaid
graph RL;
conract_emp.sql -->EMPLOYEE;
DEPT -->conract_emp.sql:::sqlClass;
BUS_UNIT -->conract_emp.sql:::sqlClass;
CONTRACT_EMP_STG -->conract_emp.sql:::sqlClass;
perm_emp.sql -->EMPLOYEE;
PERM_EMP_STG -->perm_emp.sql:::sqlClass;
DEPT -->perm_emp.sql:::sqlClass;
BUS_UNIT -->perm_emp.sql:::sqlClass;
dept.sql -->DEPT;
DEPT_STG -->dept.sql:::sqlClass;
COMPENSATION -->dept.sql:::sqlClass;
bus_unit.sql -->BUS_UNIT;
GEO -->bus_unit.sql:::sqlClass;
BUS_UNIT_STG -->bus_unit.sql:::sqlClass;
geo.sql -->GEO;
GEO_STG -->geo.sql:::sqlClass;
compensation.sql -->COMPENSATION;
COMPENSATION_STG -->compensation.sql:::sqlClass;
classDef sqlClass fill:#f96;
```
# Mermaid Js Link (Open Via Browser)
[Mermaid JS API](https://kroki.io/mermaid/svg/eNqFkV0LgjAUhu_9FULXdhnkIDAdIviFzouuhtk0wY_l9P-n1aktkm42OOc5z97DqiHnVz3xkVb03ZAXI2Ut34pboxvGAQexH50wRpqDY7JUviDTNOfTbnIhkHbMUpqF3l_OjkKSWDahs56mxP3Hcza0v1PFOAlki0wqCoi_CsjZV6EL4yOEWIxPLzwO3a9dgxiHqUW8KFyFzpOgU1e_3RAGaS6OloIM_IwNGVbBivVgn50PMcy8Wgpe9C1nncjHuu9gTl5FXezzieqUqlwuh5U6lPSybhpzU-536A5QztL-)