CREATE TABLE public.customer (
  id BIGSERIAL constraint pk_customer PRIMARY KEY,
  name varchar(255) not NULL,
  email varchar(255) not null,
  address varchar(255) not null,
  phone varchar(255) not null,
  city varchar(255) not null,
  state varchar(255) not null,
  zip_code varchar(255) not null
);


CREATE TABLE public.book (
  id BIGSERIAL constraint pk_book PRIMARY KEY,
  publisher_name varchar(255) not NULL,
  author_name varchar(255) not null,
  publisher varchar(255) not null,
  customer_review varchar(255) not null
);

CREATE TABLE public.book_transaction (
  id BIGSERIAL constraint pk_bt PRIMARY KEY,
  customer_transaction_id int REFERENCES customer_transaction (id),
  book_id int REFERENCES book (id)
);

CREATE TABLE public.customer_transaction (
  id BIGSERIAL constraint pk_ct PRIMARY KEY,
  customer_id int REFERENCES customer (id)
);


CREATE TYPE transaction_status AS ENUM ('in progress', 'completed', 'cancelled');
ALTER TABLE customer_transaction ADD COLUMN status transaction_status DEFAULT 'in progress';


ALTER SEQUENCE customer_id_seq restart WITH 1;
ALTER SEQUENCE book_id_seq restart WITH 1;
ALTER SEQUENCE book_transaction_id_seq restart WITH 1;
ALTER SEQUENCE customer_transaction_id_seq restart WITH 1;

UPDATE customer SET id=nextval('pk_customer');
