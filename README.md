# Fome Zero Dashboard

Com este projeto temos o intuito de montar um dashboard entregue hosteado no Streamlit, com uma base de dados retirada do Kaggle neste [link](https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset).  

Esta base de dados é de um aplicativo de avaliação de restaurantes, com dados de quase 7000 restaurantes!  

Foram utilizadas técnicas de manipulação de dados com **Pandas** para limpar a base de dados, criação de elementos gráficos com o **Plotly**, criação de mapa com o **Folium** e apresentação com o **Streamlit**.

Para a criação do mapa, achei muito útil [este artigo](https://python-graph-gallery.com/312-add-markers-on-folium-map/) do [Yan Holtz](https://www.yan-holtz.com).

---

O Dashboard pode ser encontrado [aqui](https://fomezerodashapp.streamlit.app) e conta, por hora, com 3 páginas.

Na página inicial nós temos algumas métricas sobre o banco de dados, como quantidade de restaurantes cadastrados, quantidade de avaliações recebeidas e quantidade de cidades que participam do projeto. Além disso, temos o mapa com marcadores agrupados, onde cada um representa um restaurante.  
A apresentação dos marcadores no mapa é filtrada pelo filtro de países na barra lateral, enquanto os dados superiores (gerais do df) não.

Na página de métricas globais nós temos alguns gráficos, apresentando a quantidade de cidades por país, a quantidade de restaurantes com nível máximo de preço por país, quantos tipos de cozinha podemos encontrar por país e o preço médio por prato para duas pessoas.  
Ressalto que o preço médio está com os valores na moeda local, então o gráfico não serve muito para comparação entre os países. Numa próxima iteração do projeto, seria interessante realizar a dolarização desses preços, para comparar todos utilizando a mesma métrica.

Temos também uma página apresentando métricas por cidade. Nela conseguimos encontrar gráficos apresentando em quais cidades do aplicativo temos mais restaurantes com avaliação média acima de 4, cidades com mais tipos diferentes de gastronomia e cidades com a maior média de avaliação. Além disso, para os amantes de restaurantes mais caros ou de restaurantes mais baratos, temos dois gráficos apresentando as 15 cidades com mais restaurantes de alta gastronomia e as 15 cidades com mais restaurantes de baixa gastronomia.  
Numa próxima iteração do projeto, eu gostaria de criar uma página de dashboard completamente voltada para restaurantes mais baratos e restaurantes mais caros, atendendo a necessidade de pessoas de ambos os gostos.

---

Além dos pontos apresentados de possiveis melhoras, também penso em gerar mais algumas páginas, mostrando algumas métricas voltadas para tipos diferentes de culinária apresentados, um *Hall of Fame*, mostrando os restaurantes mais bem avaliados e talvez colocar mais algumas possibilidades de filtro, como por nota e preço, nas páginas apresentadas. 

Qualquer dúvida sobre o projeto e/ou sugestões, fico à vontade para conversar pelo [LinkedIn](https://www.linkedin.com/in/filipesaladini/).
