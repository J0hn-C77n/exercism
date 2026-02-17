/*
Package weather provides tools to return weather forecast
on a specific location at the current moment of time, using
the CurrentCondition and CurrentLocation variables.
*/
package weather

var (
    // CurrentCondition is responsible for telling the weather condition in Forecast function. Type: str.
	CurrentCondition string
    // CurrentLocation is responsible for telling location of the weather in Forecast function. Type: str.
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
