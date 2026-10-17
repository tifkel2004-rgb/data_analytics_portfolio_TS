with source as (
    select * from {{ source('raw_workforce', 'hr_dataset_raw') }}
),

renamed as (
    select
        -- Keys
        cast(employee_id as string) as employee_id,
        
        -- Employee Demographics & Attributes
        cast(age as integer) as employee_age,
        cast(gender as string) as gender,
        cast(marital_status as string) as marital_status,
        
        -- Professional Metrics
        cast(department as string) as department,
        cast(job_role as string) as job_role,
        cast(years_at_company as integer) as tenure_years,
        cast(monthly_income as numeric) as monthly_income_amount,
        
        -- Operational Risk Logs (Null Handling)
        coalesce(cast(attrition as string), 'No') as is_attrited,
        coalesce(cast(job_satisfaction as integer), 3) as job_satisfaction_score,
        coalesce(cast(work_life_balance as integer), 3) as work_life_balance_score

    from source
)

select * from renamed
