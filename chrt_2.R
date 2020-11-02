library(ggplot2)
library(plotly)
scatter <- function(dataset) {
  p <- ggplot(dataset, aes(Freedom, Happiness.Score
                           , colour = Trust..Government.Corruption.
                           , text = paste("Country:", Country))) + geom_point()
  tog <- p + ggtitle("Freedom vs Happiness") +
    xlab("Happiness") +
    ylab("Freedom") +
    labs(color = "Trust in Government")
  return(ggplotly(tog))
}
