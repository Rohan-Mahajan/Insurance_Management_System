SQL Schemas

create database InsuranceManagementSystem;

use InsuranceManagementSystem;

create table Users(
    user_id int primary key,
	user_name varchar(85),
	user_password varchar(85),
	user_role varchar(20)
);

create table policy(
    policy_id int primary key, 
	policy_name varchar(85),
	premium_cost decimal(12,2),
	coverage_limit decimal(12,2)
);

create table client(
    customer_id int primary key,
	customer_name varchar(120),
	contact_details varchar(120),
	policy_id int,
	constraint fk_client_policy foreign key(policy_id)
	references policy(policy_id)
);

create table claim(
    claim_id int primary key,
	claim_num varchar(85),
	file_date Date,
	amount decimal(12,3),
	claim_status varchar(20),
	policy_ID int, 
	customer_id int,
	constraint fk_claim_client foreign key(customer_id)
	references client(customer_id)
);

create table payment(
    transaction_id int primary key,
	transaction_date date,
	transaction_amount decimal(12,2),
	customer_id int,
	constraint fk_payment_client foreign key (customer_id)
	references client(customer_id)
);

Screenshots

1. Creating Policy

![image](https://github.com/user-attachments/assets/f4677077-93c4-4dc3-8e69-5d32d9a42453)


Result:-

![image](https://github.com/user-attachments/assets/162750bf-2714-4f87-ab58-8787e28be571)

2. Get Policy by ID

![image](https://github.com/user-attachments/assets/188e549e-6d24-4c75-9d53-c88fc4fffbe9)

Result:-

![image](https://github.com/user-attachments/assets/f19e80b4-6f36-4ce8-b1f3-5078543d4f54)

3. Get All Policies 

![image](https://github.com/user-attachments/assets/a11134fb-9de4-457a-a38f-a809af37e781)

Result:-

![image](https://github.com/user-attachments/assets/2945121f-8719-4a91-9517-f2cded4c150f)

4. Updating Policy

 ![image](https://github.com/user-attachments/assets/42bd20d3-9cc9-4707-b582-06e964b85fa2)

 Result:-
 Previous data ->
 
![image](https://github.com/user-attachments/assets/35ad9a44-1e4a-4639-afc2-618b287c9f1a)

Updates data ->

![image](https://github.com/user-attachments/assets/3c059464-2cda-4eb8-b018-2ccebcfb4513)

5. Deleting Policy 

![image](https://github.com/user-attachments/assets/92ddfa38-0dbf-408f-a4b3-ef58993e5657)

Result:- 

![image](https://github.com/user-attachments/assets/09e1cc1a-8276-444f-9eba-8073419268ac)

6. Policy Not Found Exception

![image](https://github.com/user-attachments/assets/77144ff4-9957-4cb6-b394-e5f8a845ef12)

7. Exit
   
![image](https://github.com/user-attachments/assets/91d8fd91-1fee-4f6b-afad-03016e09bbfd)

