-- Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT t.fullname, ROUND(AVG(g.grade), 2)
FROM teachers t 
JOIN disciplines d ON d.teacher_id = t.id 
JOIN grades g ON g.disciplines_id = d.id 
WHERE t.id = 3