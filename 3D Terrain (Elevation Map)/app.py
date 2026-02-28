import pydeck as pdk

# Configuração da camada de terreno (TerrainLayer)
terrain = pdk.Layer(
    "TerrainLayer",
    elevation_data="https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png",
    texture="https://a.tile.openstreetmap.org/{z}/{x}/{y}.png",
    elevation_decoder={"rScaler": 256, "gScaler": 1, "bScaler": 1/256},
    elevation_scale=30
)

# Configuração da visualização inicial (Câmera)
view_state = pdk.ViewState(
    latitude=37.76,
    longitude=-122.42,
    zoom=11,
    pitch=45
)

# Criação do Deck
deck = pdk.Deck(
    layers=[terrain],
    initial_view_state=view_state
)

# Gera o arquivo HTML
deck.to_html("meu_mapa_3d.html")

print("Arquivo 'meu_mapa_3d.html' gerado com sucesso!")