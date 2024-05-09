select order_id, product_id, date_format('%Y-%m-%d', out_date) as out_date,
       case
           when out_date <= '2022-05-01' then '출고완료'
           when out_date > '2022-05-01' then '출고대기'
           else '출고미정'
        end 출고여부
from food_order
order by order_id
