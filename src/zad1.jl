begin 
    using Plots 
    using CSV
    using DataFrames
    using Dates
    using TimeSeries
end

electricity_data = CSV.read("electricity_prices_day_ahead_hourly_all.csv", DataFrame)
electricity_data = electricity_data[1:17543, :]


plot(electricity_data[!, :fixing_i_price])
