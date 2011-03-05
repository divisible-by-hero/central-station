create table comments(
comment_id int not null auto_increment,
module_id int not null,
item_id int not null,
comment big_blob null,
commenter_email text,
commenter_first_name text,
commenter_last_name text,
comment_date date,
PRIMARY KEY(comment_id)
);