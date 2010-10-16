-- Forum

-- Reply table

drop if exists forumReply;


create table forumReply(
replyID int auto_increment not null,
replyUserID int not null,
replyTitle varchar(256) not null,
replyContent blob not null,
PRIMARY KEY (replyID)
);

