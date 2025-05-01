-- employees 테이블을 생성
CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100),
	position VARCHAR(100),
	salary DECIMAL(10, 2)
);

-- 직원데이터를 employees에 추가해주세요
insert into employees (name, position, salary) values('혜린', 'PM', 90000);
insert into employees (name, position, salary) values('은우', 'Frontend', 80000);
insert into employees (name, position, salary) values('가을', 'Backend', 92000);
insert into employees (name, position, salary) values('지수', 'Frontend', 78000);
insert into employees (name, position, salary) values('민혁', 'Frontend', 96000);
insert into employees (name, position, salary) values('하온', 'Backend', 130000);
 
 -- 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리 작성
 SELECT * FROM employees;

-- Forntend 직책을 가진 직원주에서 연봉이 90000이하인 직원의 이름과 연봉을 조회
 SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;
 
 -- PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인
UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM';
SELECT * FROM employees WHERE position = 'PM';

-- 모든 Backend 직책을 가진 직원의 연봉을 5% 인상
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';

-- 민혁 사원의 데이터를 삭제하세요.
DELETE FROM employees WHERE name = '민혁';

-- 모든 직원을 position별로 그룹화하여 각 직책의 평균 연봉을 계산
SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;

-- employees 테이블 삭제
DROP TABLE employees;
