TRUNCATE COMPENSATION
INSERT INTO COMPENSATION SELECT DEPT, GRADE, COMPENSATION FROM COMPENSATION_STG WHERE DELETE_DTM IS NOT NULL;