* Daily Stock Changes

   - The focus on this report will be anaylzing how stocks change throughout the day. The structure seperates the ticker data from the prices. By removing the idnetifying companies from the market data the trends of recurring stocks and the pricing over times are highlighted. The goal is to identify the potential opportunies in stock based off of frequency and composition.

* Use cases:

   - Compare different companies of the same industry. The data has some recurring symbols that may be of interest to pick stocks that show up frequently.
   - To look at a daily summary of stock prices which includes the volume, volume change, and percent change.
   - Can look at how a specific event affected stock by comparing the daily summaries of before/after specific days.
   
* Methods:

The raw html is pulled from the web and then the table info is isolated and converted into a csv file. This is then normalized by formatting the columns and removing unnecessary columns. Then when inputing into the database, each entry is split into two datasets that are linked. One is the name and ticker symbol while the other has the numerical data that includes the volume, last trade, change, and percent change.

* Summary 

Seperating the company from the price info give flexiblity to analysize the stock gainers. This will help identify patterns like frequently occuring symbols and and diving the gainers based on price ranges. This will help in creating better hypothesis generation for short term trading.
This can then be built into merging with additional data to expand the anaysis.

```
erDiagram
    COMPANY ||--o{ TICKER : has
    TICKER ||--o{ PRICE_RECORD : logs

    COMPANY {
        int id
        string name
    }

    TICKER {
        string symbol PK
        int company_id FK
        string exchange
    }

    PRICE_RECORD {
        string date PK
        string symbol FK
        float volume
        float last_price
        float change
        float percent_change
    }
```
