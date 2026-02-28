// Package weather provides tools to return weather forecast
// on a specific location at the current moment of time, using
// the CurrentCondition and CurrentLocation variables.
package weather

var (
    // CurrentCondition is responsible for storing weather.
	CurrentCondition string 
    // CurrentLocation is responsible for storing Place of the forecast.
	CurrentLocation  string 
)

/*
Forecast fucntion returns the city of the forecast and the condition of
the weather in the described city.
*/
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
