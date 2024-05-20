USE [KhakRusDict]
GO

SELECT  [id], [entry]
FROM [KhakRusDict].[dbo].[Entry]
GO
DELETE
FROM [KhakRusDict].[dbo].[Entry] 
GO


ALTER TABLE dbo.[Entry] 
ALTER COLUMN [entry] Ntext COLLATE Latin1_General_100_CI_AI_SC_UTF8
GO




/* Просто SELECT */
SELECT  [id], [entry]
FROM [KhakRusDict].[dbo].[Entry]
GO


/* WHERE & JOIN - выбор глаголов с русским происхождением */
SELECT [word], [translation]
FROM [Word]
JOIN [Other] ON ([Word].[id]=[Other].[id])
	WHERE ([Other].[etymology] = 'rus') AND ([Other].[part] = 'VERBUM')
GO

/* COUNT - количество неизменяемых слов */
SELECT
	[Неизменяемые] = COUNT ([Other].[part])
FROM [Other]
WHERE ([Other].[part] = 'INVAR' OR [Other].[part] = 'INVAR1')

GO

/* ORDER BY - сортировка по переводу */
SELECT [translation], [word], [entry]
FROM [Other]
JOIN [Word] ON ([Word].[id]=[Other].[id])
JOIN [Entry] ON ([Other].[id]=[Entry].[id])
ORDER BY [Other].[translation]
GO

/*CROSS JOIN, UNION, EXCEPT, INTERSECT, IF, THEN, CASE (END), BETWEEN, ORDER BY, HAVING, IIF*/
/* CASE - определение изменяемых и неизменяемых слов */
SELECT 
CASE
	WHEN [Other].[part] = 'INVAR' OR [Other].[part] = 'INVAR1'
	THEN 'Незменяемый'
	ELSE 'Изменяемый'
END, [word]
FROM [Other] JOIN [Word] ON ([Other].[id]=[Word].[id])
GO


/* BETWEEN - выбор слов с П по С */
SELECT [word], [entry]
FROM [Word] JOIN [Entry] ON ([Word].[id]=[Entry].[id])
WHERE ([Word].[word] BETWEEN 'п' AND 'с')
ORDER BY [Word].[word]
GO

/* CROSS JOIN */
SELECT TOP 20 [word], [alt_word], [entry]
FROM [Word]
CROSS JOIN [Entry]
WHERE ([Word].[alt_word] != ' ')
GO

/* UNION - количество глаголов и существительных */
SELECT [Количество глаголов и сущестительных] = COUNT ([id])
FROM [Other]
WHERE ([Other].[part]='VERBUM')
UNION
SELECT [Количество имён] = COUNT ([id])
FROM [Other]
WHERE ([Other].[part]='NOMEN')
GO

/* EXCEPT & INTERSECT - без имен; только имена */
SELECT [Word].[id],[word]
FROM [Word] JOIN [Other] ON ([Word].[id]=[Other].[id])
EXCEPT
SELECT [Word].[id],[word]
FROM [Word] JOIN [Other] ON ([Word].[id]=[Other].[id])
WHERE ([Other].[part]='NOMEN')

SELECT [Word].[id],[word]
FROM [Word] JOIN [Other] ON ([Word].[id]=[Other].[id])
INTERSECT
SELECT [Word].[id],[word]
FROM [Word] JOIN [Other] ON ([Word].[id]=[Other].[id])
WHERE ([Other].[part]='NOMEN')
GO

/* GROUP BY & HAVING - омонимичные слова */
SELECT [word], [количество омонимичных значений] = COUNT (*)
FROM [Word] JOIN [Other] ON ([Word].[id]=[Other].[id])
GROUP BY [word]
HAVING COUNT (*) > 1
ORDER BY [word]
GO

/* IIF - определение части речи */
SELECT [word], IIF([Other].[part]='VERBUM','Глагол', 'Имя')
FROM [Word] JOIN [Other] ON ([Word].[id]=[Other].[id])
WHERE ([part] != 'INVAR' OR [part] != 'INVAR1')
GO

/* INNER JOIN - тут должно было быть пересечение на выборке алы... */
SELECT [word] AS [Слова], [morphs] AS [Морфемы]
FROM [Word] INNER JOIN [Morphemes] ON ([Word].[id]=[Morphemes].[id])
WHERE ([word] LIKE 'алы%')
GO


/*OTHER*/
SELECT [translation], [word], [morphs_tags]
FROM [Other] JOIN [Word] ON ([Other].[id]=[Word].[id]) JOIN [Morphemes] ON ([Word].[id]=[Morphemes].[id])
WHERE ([Word].[word]='истіг')
GO


/* переменная */
DECLARE @ID INT;
SET @ID = ROUND(22190*RAND(),0);
SELECT [id], [word]
FROM [Word]
WHERE ([id]=@ID)
GO


SELECT ROUND(123.9994, 0), ROUND(123.9995, 0);  
GO