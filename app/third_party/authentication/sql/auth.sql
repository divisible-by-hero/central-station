CREATE TABLE IF NOT EXISTS `auth` (
    user_id INT NOT NULL AUTO_INCREMENT,
    username varchar(40) NOT NULL,
    email varchar(50) NOT NULL,
    password varchar(40) NOT NULL,
    salt varchar(40) NOT NULL,
    status INT DEFAULT 0 NOT NULL,
    first_name varchar(250) not null,
    last_name varchar(250) not null,
    PRIMARY KEY (user_id)
);