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

