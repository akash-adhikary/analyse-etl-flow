# Mermaid Js Diagram for EMPLOYEE_DETAILS
```mermaid
graph LR;
EMPLOYEE_DETAILS -->conract_emp.sql;
conract_emp.sql:::sqlClass -->BUS_UNIT;
conract_emp.sql:::sqlClass -->CONTRACT_EMP_STG;
conract_emp.sql:::sqlClass -->DEPT;
EMPLOYEE_DETAILS -->perm_emp.sql;
perm_emp.sql:::sqlClass -->BUS_UNIT;
perm_emp.sql:::sqlClass -->DEPT;
perm_emp.sql:::sqlClass -->PERM_EMP_STG;
BUS_UNIT -->bus_unit.sql;
bus_unit.sql:::sqlClass -->GEO;
bus_unit.sql:::sqlClass -->BUS_UNIT_STG;
DEPT -->dept.sql;
dept.sql:::sqlClass -->COMPENSATION;
dept.sql:::sqlClass -->DEPT_STG;
COMPENSATION -->compensation.sql;
compensation.sql:::sqlClass -->COMPENSATION_STG;
GEO -->geo.sql;
geo.sql:::sqlClass -->GEO_STG;
classDef sqlClass fill:#f96;
```
# Mermaid Js Link (Open Via Browser)
[Mermaid JS API](https://kroki.io/mermaid/svg/eNqFUcsKgzAQvPsVQs_2WGiEgtUggi80HnoK1kYr-EiN_n8N0Wq12kvYnR1mZrNZE9OnbAeqBB3f9m4QYgMizbJDWVEuSV01cdJiUtIjexWqtAAAAP2rFzFjnH6NQhy5FvrH0z0XBZqOcO-JQ2T-4xvQR78DUtKUU7p5txlthyR8dgg-DJwp9KjJJ_eO4a7KWxFk3i0kTOjtzkdRYcETcfRB6CA9VqsvdXzohhqyPHeTxNWE7pwuDl1SUrG4zetqvPQ3suMnJPvF-CAjtRAYivX6w8U5YpBU_kzTvCjAIT2f1DeqQNfI)