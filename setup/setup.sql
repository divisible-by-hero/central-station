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

-- Settings to add

insert into settings('settingName', 'settingValue') VALUES('forumName', 'Bobs Forum');
insert into settings('settingName', 'settingValue') values('defectName', 'Defect');
