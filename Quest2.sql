SELECT track,
       CASE
			WHEN cancelled = TRUE THEN -1 
			WHEN finished = TRUE THEN 2 
			WHEN "inDelivery" = TRUE THEN 1 
			ELSE 0 
		END
FROM "Orders";