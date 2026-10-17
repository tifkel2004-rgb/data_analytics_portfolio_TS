with employees as (
    select * from {{ ref('stg_workforce__employees') }}
),

calculated_risk as (
    select
        employee_id,
        employee_age,
        department,
        job_role,
        tenure_years,
        monthly_income_amount,
        is_attrited,
        
        -- Analytics Logic: Flagging potential burnout environments
        case 
            when work_life_balance_score <= 2 and job_satisfaction_score <= 2 then 'High Risk'
            when work_life_balance_score = 3 or job_satisfaction_score = 3 then 'Medium Risk'
            else 'Low Risk'
        end as burnout_risk_tier,

        -- Salary Ceiling Flag (Evaluating relative compensation depth)
        case 
            when monthly_income_amount >= 15000 then 'Tier 1 (Executive)'
            when monthly_income_amount >= 8000 and monthly_income_amount < 15000 then 'Tier 2 (Senior)'
            else 'Tier 3 (Associate)'
        end as compensation_band

    from employees
)

select * from calculated_risk
Add dbt core workforce attrition fact table
