
select count(*) as row_count
from {{ source('raw', 't') }}
