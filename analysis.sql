-- Create sample table and insert data
CREATE TABLE remote_work_ai_2025 (
    Month VARCHAR(10),
    Productivity_Increase_Pct FLOAT,
    Meeting_Time_Reduction_Pct FLOAT,
    Tech_Fatigue_Pct FLOAT
);

INSERT INTO remote_work_ai_2025 (Month, Productivity_Increase_Pct, Meeting_Time_Reduction_Pct, Tech_Fatigue_Pct) VALUES
('Jan-25', 30, 18, 12),
('Feb-25', 32, 19, 13),
('Mar-25', 33, 20, 14),
('Apr-25', 34, 20, 15),
('May-25', 35, 21, 15),
('Jun-25', 35, 20, 16),
('Jul-25', 34, 19, 16),
('Aug-25', 35, 20, 15);

-- Query for averages
SELECT 
    AVG(Productivity_Increase_Pct) AS Avg_Productivity,
    AVG(Meeting_Time_Reduction_Pct) AS Avg_Meeting_Reduction,
    AVG(Tech_Fatigue_Pct) AS Avg_Tech_Fatigue
FROM remote_work_ai_2025;

-- Query for trends (month-over-month change in productivity)
SELECT 
    Month,
    Productivity_Increase_Pct,
    Productivity_Increase_Pct - LAG(Productivity_Increase_Pct, 1, 0) OVER (ORDER BY Month) AS Productivity_Change
FROM remote_work_ai_2025;