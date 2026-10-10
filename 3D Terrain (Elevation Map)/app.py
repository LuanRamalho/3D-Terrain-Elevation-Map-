import pydeck as pdk

# ============================================================
# 1. FONTES DE DADOS
# ============================================================

# Modelo digital de elevação Terrarium.
# Os tiles fornecem as alturas utilizadas para construir o relevo.
ELEVATION_DATA = (
    "https://s3.amazonaws.com/elevation-tiles-prod/"
    "terrarium/{z}/{x}/{y}.png"
)

# Mapa de ruas da Esri, sem necessidade de inserir uma chave
# de API neste endereço público.
# A ordem dos índices da Esri é z/y/x.
TEXTURE_DATA = (
    "https://server.arcgisonline.com/ArcGIS/rest/services/"
    "World_Street_Map/MapServer/tile/{z}/{y}/{x}"
)

# ============================================================
# 2. CAMADA DE TERRENO TRIDIMENSIONAL
# ============================================================

terrain = pdk.Layer(
    "TerrainLayer",
    id="terreno-3d",

    elevation_data=ELEVATION_DATA,
    texture=TEXTURE_DATA,

    # Decodificador correto para os dados de elevação Terrarium
    elevation_decoder={
        "rScaler": 256,
        "gScaler": 1,
        "bScaler": 1 / 256,
        "offset": -32768
    },

    # Exagero vertical moderado para destacar o relevo
    elevation_scale=2.0,

    # Precisão da malha 3D
    mesh_max_error=4,

    # Iluminação e sombreamento do terreno
    material=True,

    # Limita a solicitação de elevação ao nível máximo 15
    max_zoom=15
)

# ============================================================
# 3. CÂMERA INICIAL
# ============================================================

view_state = pdk.ViewState(
    latitude=37.76,
    longitude=-122.42,
    zoom=11,
    pitch=60,
    bearing=0,

    # Limita o zoom aos níveis de elevação disponibilizados
    # pela fonte, evitando solicitar detalhes inexistentes.
    min_zoom=6,
    max_zoom=15
)

# ============================================================
# 4. CRIAÇÃO DO MAPA
# ============================================================

deck = pdk.Deck(
    layers=[terrain],
    initial_view_state=view_state,

    # Impede o carregamento do mapa-base padrão do PyDeck.
    # A textura da camada 3D continua ativa.
    map_provider=None,
    map_style=None,

    width="100%",
    height=760
)

# ============================================================
# 5. GERAÇÃO DO HTML
# ============================================================

arquivo = "mapa_3d.html"

deck.to_html(
    filename=arquivo,
    open_browser=True,
    css_background_color="#eaf0f5"
)

print(f"Mapa 3D gerado com sucesso: {arquivo}")
