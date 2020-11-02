library(leaflet)
library(dplyr)

interactive_map <- function(dataset) {
  twensev_data <- dataset %>%
    group_by(Country) %>%
    filter(Happiness.Rank < 11) %>%
    mutate(on_hover = paste0(
      "Country: ", Country, "<br>",
      "Happiness Rank: ", Happiness.Rank, "<br>"
    ))
  hap_map <- leaflet(twensev_data) %>%
    addTiles() %>%
    addCircleMarkers(
      radius = ~ 10,
      lat = ~ c(60.472023, 56.26392, 64.963051,
                46.818188, 61.92411, 52.132633,
                56.130366, -40.900557, 60.128161,
                -25.274398),
      lng = ~ c(8.468946, 9.501785, -19.020835,
                8.227512, 25.748151, 5.291266,
                -106.346771, 174.885971, 18.643501,
                133.775136),
      stroke = FALSE,
      fillOpacity = 0.5,
      popup = ~on_hover
    )
  return(hap_map)
}
