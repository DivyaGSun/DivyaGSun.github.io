library(plotly)
library(dplyr)
bar_chart <- function(dataset) {
  x_graph <- dataset %>%
  group_by(Country) %>%
  pull(Country)
  y_graph <- dataset %>%
  group_by(Country) %>%
  pull(Economy..GDP.per.Capita.)
  final_graph <- dataset %>%
  plot_ly(
    type = "bar",
    x = ~factor(x_graph, levels = x_graph),
    y = ~y_graph,
    color = ~x_graph,
    colors = "Paired"
  ) %>%
  layout(
    title = "Economy of Happiest to Unhappiest Countries (2017)",
    xaxis = list(
      title = "Country: Happiest to Unhappiest (Left to Right)"
    ),
    yaxis = list(
      title = "Economy"
    )
  )
 return(final_graph)
}
