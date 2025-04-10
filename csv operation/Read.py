import pandas as pd
dis = {
    "symbol": ["@", "@$", "@#", "@%", "@^", "@&", "@*", "@!", "@~", "@`",
               "@1", "@2", "@3", "@4", "@5", "@6", "@7", "@8", "@9", "@0",
               "@a", "@b", "@c", "@d", "@e", "@f", "@g", "@h"],
    
    "security": ["AAPL", "MSFT", "AMZN", "GOOGL", "TSLA", "FB", "NFLX", "NVDA", "INTC", "AMD",
                 "BABA", "ORCL", "IBM", "SAP", "ADBE", "CRM", "UBER", "LYFT", "SHOP", "SQ",
                 "ZM", "TWTR", "PINS", "SNAP", "ROKU", "COIN", "PLTR", "NET"],
    
    "today": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25, 26, 27, 28],
    
    "avg volume": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                   1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
                   2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800],
    
    "charges": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
                210, 220, 230, 240, 250, 260, 270, 280]
}
d = pd.DataFrame(dis)
print(d)
d.to_csv("data.csv")
d.to_csv("without_index.csv", index=False)
d.to_csv("without_header.csv", header=False)
