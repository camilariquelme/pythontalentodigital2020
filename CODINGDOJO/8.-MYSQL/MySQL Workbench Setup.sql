use twitter;
select * from users;
insert into users (id, first_name, last_name, handle, birthday,created_at,updated_at)
values (6, "camila", "riquelme","campaz",now(),now(),now());
select * from users;
update users set
first_name = "paz"
where id=6;
select * from users;
delete from users
where id = 6;
select * from users;

