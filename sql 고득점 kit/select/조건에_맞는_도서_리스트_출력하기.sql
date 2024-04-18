select b.book_id, date_format(b.published_date, '%Y-%m-%d') as published_date
from book b
where b.category = '인문' and year(published_date)=2021
order by published_date
