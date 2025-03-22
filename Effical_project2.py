import streamlit as st
import time
#import  as st
import pandas as pd

st.set_page_config(
    page_title="EffiCal - Calcul thermique des bâtiments selon le DTR C3.2/4",
    layout="wide",
    initial_sidebar_state="expanded"
)
with st.spinner("Chargement en cours..."):
    time.sleep(3)  # Simuler un délai de chargement
st.image("https://raw.githubusercontent.com/hdahhaoui/effical_image.git", width=500)
st.success("Chargement terminé !")
resistance_des_murs = {}
# Liste pour stocker les matériaux avec leur épaisseur
nom_mat_epai = []
# la liste des materiaux et leur conductivite
materiaux = {
    "Mortier de chaux": {"conductivite": 0.87, "masse volumique": 1800},
    "Carreaux de plâtre pleins .": {"conductivite": 1.4, "masse volumique": 950},
    "Liège Comprimé": {"conductivite": 0.1, "masse volumique": 500},
    "Expansé pur": {"conductivite": 0.044, "masse volumique": 130},
    "Verre .": {"conductivite": 0.80, "masse volumique": 1900},
    "crépis": {"conductivite": 0.84, "masse volumique": 3800},
    "Mortier de ciment": {"conductivite": 1.4, "masse volumique": 2200},
    "Lame d'air": {"conductivite": 1, "masse volumique": 1},
    "Enduit platre": {"conductivite": 0.35, "masse volumique": 1300},
    "Enduit de ciment ": {"conductivite": 0.87, "masse volumique": 1400},
    "Béton lourd 1": {"conductivite": 1.75, "masse volumique": 2350},
    "Béton pleine ": {"conductivite": 1.75, "masse volumique": 2200},
    "Béton lourd 2": {"conductivite": 1.29, "masse volumique": 2350},
    "Brique creuses": {"conductivite": 0.48, "masse volumique": 900},
    "Brique pleine 1 ": {"conductivite": 0.8, "masse volumique": 1700},
    "Brique pleine 2 ": {"conductivite": 1.00, "masse volumique": 1900},
    "Brique pleine 3 ": {"conductivite": 1.10, "masse volumique": 2000},
    "Carrelage": {"conductivite": 2.10, "masse volumique": 1900},
    "Sable sec": {"conductivite": 0.60, "masse volumique": 1300},
    "Gravillon": {"conductivite": 2, "masse volumique": 1500},
    "Mousse de polyréthan 1": {"conductivite": 0.031, "masse volumique": 29},
    "Mousse de polyréthan 2": {"conductivite": 0.034, "masse volumique": 50},
    "Laine de roche 1": {"conductivite": 0.047, "masse volumique": 23},
    "Laine de roche 2": {"conductivite": 0.041, "masse volumique": 30},
    "Laine de roche 3": {"conductivite": 0.038, "masse volumique": 58},
    "Laines de verre": {"conductivite": 0.044, "masse volumique": 9},
    "Fer pur": {"conductivite": 72, "masse volumique": 7870},
    "Acier": {"conductivite": 52, "masse volumique": 7780},
    "Fonte": {"conductivite": 56, "masse volumique": 7500},
    "Alluminium": {"conductivite": 230, "masse volumique": 2700},
    "Cuivre": {"conductivite": 380, "masse volumique": 8930},
    "Plomb": {"conductivite": 35, "masse volumique": 11340},
}
#st.title("Mon application EffiCal")
#st.write("Bienvenue !")
# Navigation via la sidebar
page = st.sidebar.radio("Navigation", ["Accueil", "Calcul", "Résultats"])

if page == "Accueil":
    st.title("EffiCal - Calcul thermique des bâtiments")
    st.write("Bienvenue dans l'application EffiCal. Utilise la barre latérale pour naviguer entre les sections.")
elif page == "Calcul":
    st.title("Calcul")
    st.write("Ici se trouvent les outils de calcul.")
elif page == "Résultats":
    st.title("Résultats")
    st.write("Affichage des résultats.")

# Créer un menu de navigation dans la sidebar pour simuler plusieurs pages
page = st.sidebar.radio("Navigation", ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6"])

if page == "Page 1":
    st.title("Page 1 - Accueil")
 #   st.write("Contenu de la page 1.")
elif page == "Page 2":
    st.title("Page 2 - Calcul")
  #  st.write("Contenu de la page 2.")
elif page == "Page 3":
    st.title("Page 3 - Données")
  #  st.write("Contenu de la page 3.")
elif page == "Page 4":
    st.title("Page 4 - Informations")
  #  st.write("Contenu de la page 4.")
elif page == "Page 5":
    st.title("Page 5 - Résultats")
 #   st.write("Contenu de la page 5.")
elif page == "Page 6":
    st.title("Page 6 - Autres")
 #   st.write("Contenu de la page 6.")


#import  as st

# Option de thème via la sidebar
use_green_theme = st.sidebar.checkbox("Activer le thème vert attractif", value=True)

if use_green_theme:
    st.markdown(
        """
        <style>
        /* Thème vert attractif : fond vert et texte blanc */
        body {
            background-color: #27ae60;
            color: #ffffff;
        }
        .stApp {
            background-color: #27ae60;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        /* Thème par défaut clair */
        body {
            background-color: #ffffff;
            color: #000000;
        }
        .stApp {
            background-color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# st.write("Votre application avec un thème vert attractif est active.")



#import  as st
#import pandas as pd

# Exemple du dictionnaire de matériaux (assurez-vous que cette variable existe déjà dans votre code)
materiaux = {
    "Mortier de chaux": {"conductivite": 0.87, "masse volumique": 1800},
    "Carreaux de plâtre pleins .": {"conductivite": 1.4, "masse volumique": 950},
    "Liège Comprimé": {"conductivite": 0.1, "masse volumique": 500},
    "Expansé pur": {"conductivite": 0.044, "masse volumique": 130},
    "Verre .": {"conductivite": 0.80, "masse volumique": 1900},
    "crépis": {"conductivite": 0.84, "masse volumique": 3800},
    "Mortier de ciment": {"conductivite": 1.4, "masse volumique": 2200},
    "Lame d'air": {"conductivite": 1, "masse volumique": 1},
    "Enduit platre": {"conductivite": 0.35, "masse volumique": 1300},
    "Enduit de ciment ": {"conductivite": 0.87, "masse volumique": 1400},
    "Béton lourd 1": {"conductivite": 1.75, "masse volumique": 2350},
    "Béton pleine ": {"conductivite": 1.75, "masse volumique": 2200},
    "Béton lourd 2": {"conductivite": 1.29, "masse volumique": 2350},
    "Brique creuses": {"conductivite": 0.48, "masse volumique": 900},
    "Brique pleine 1 ": {"conductivite": 0.8, "masse volumique": 1700},
    "Brique pleine 2 ": {"conductivite": 1.00, "masse volumique": 1900},
    "Brique pleine 3 ": {"conductivite": 1.10, "masse volumique": 2000},
    "Carrelage": {"conductivite": 2.10, "masse volumique": 1900},
    "Sable sec": {"conductivite": 0.60, "masse volumique": 1300},
    "Gravillon": {"conductivite": 2, "masse volumique": 1500},
    "Mousse de polyréthan 1": {"conductivite": 0.031, "masse volumique": 29},
    "Mousse de polyréthan 2": {"conductivite": 0.034, "masse volumique": 50},
    "Laine de roche 1": {"conductivite": 0.047, "masse volumique": 23},
    "Laine de roche 2": {"conductivite": 0.041, "masse volumique": 30},
    "Laine de roche 3": {"conductivite": 0.038, "masse volumique": 58},
    "Laines de verre": {"conductivite": 0.044, "masse volumique": 9},
    "Fer pur": {"conductivite": 72, "masse volumique": 7870},
    "Acier": {"conductivite": 52, "masse volumique": 7780},
    "Fonte": {"conductivite": 56, "masse volumique": 7500},
    "Alluminium": {"conductivite": 230, "masse volumique": 2700},
    "Cuivre": {"conductivite": 380, "masse volumique": 8930},
    "Plomb": {"conductivite": 35, "masse volumique": 11340},
}

def filter_materiaux(search_text, data):
    """Filtre le dictionnaire des matériaux selon le texte de recherche."""
    if not search_text:
        return data
    filtered = {item: props for item, props in data.items() if search_text.lower() in item.lower()}
    return filtered

def dict_to_dataframe(data):
    """Convertit le dictionnaire des matériaux en DataFrame pour affichage."""
    df_rows = []
    for item, props in data.items():
        df_rows.append({
            "Matériau": item,
            "Conductivité (W/m.K)": props['conductivite'],
            "Masse Volumique (kg/m³)": props['masse volumique']
        })
    return pd.DataFrame(df_rows)

# Interface de recherche
search_text = st.text_input("Recherche de matériaux:")

filtered_data = filter_materiaux(search_text, materiaux)
df = dict_to_dataframe(filtered_data)

st.dataframe(df)



#import  as st

# On suppose que les variables suivantes sont gérées via st.session_state :
# - st.session_state["selected_mater_name"] : Le nom du matériau sélectionné (anciennement récupéré via tree.focus())
# - st.session_state["entry_epai"] : La saisie de l'épaisseur
# - st.session_state["nom_mat_epai"] : La liste des matériaux et épaisseurs choisis
# - st.session_state["lis_de_mat_choisi"] : La liste (ou structure) où l'on affiche les matériaux choisis

def ajouter_le_materiaux():
    """Ajoute le matériau choisi à la liste de matériaux avec son épaisseur."""
    # Récupérer le nom du matériau sélectionné
    mater_name = st.session_state.get("selected_mater_name", "")
    if not mater_name:
        st.error("Erreur : Veuillez d'abord sélectionner un matériau.")
        return

    # Récupérer l'épaisseur saisie
    epaisseur_str = st.session_state.get("entry_epai", "")
    if not epaisseur_str:
        st.error("Erreur : Veuillez saisir l'épaisseur du matériau.")
        return

    # Vérifier si l'épaisseur est un nombre
    try:
        epaisseur = float(epaisseur_str)
    except ValueError:
        st.error("Erreur : L'épaisseur doit être un nombre.")
        return

    # Ajouter le matériau et l'épaisseur à la liste
    if "nom_mat_epai" not in st.session_state:
        st.session_state["nom_mat_epai"] = []
    st.session_state["nom_mat_epai"].append((mater_name, epaisseur))

    # Vider le champ d'épaisseur après l'ajout
    st.session_state["entry_epai"] = ""

    # Mettre à jour l'affichage de la liste des matériaux choisis
    if "lis_de_mat_choisi" not in st.session_state:
        st.session_state["lis_de_mat_choisi"] = []
    st.session_state["lis_de_mat_choisi"].append(f"{mater_name} -- {epaisseur} m")

    st.success(f"Matériau '{mater_name}' avec épaisseur {epaisseur} m ajouté à la liste.")

# Exemple d'interface  pour démontrer la fonction
st.markdown("### Sélection d'un matériau")
# Sélection d'un matériau (remplace tree.focus())
materiaux_disponibles = ["Mortier de chaux", "Carreaux de plâtre pleins", "Liège Comprimé"]
selected_mat = st.selectbox("Choisissez un matériau :", options=materiaux_disponibles, key="selected_mater_name")

st.markdown("### Épaisseur du matériau (m)")
st.text_input("Épaisseur (m)", key="entry_epai")

if st.button("Ajouter matériau"):
    ajouter_le_materiaux()

st.markdown("### Liste des matériaux choisis :")
if "lis_de_mat_choisi" in st.session_state and st.session_state["lis_de_mat_choisi"]:
    for idx, item in enumerate(st.session_state["lis_de_mat_choisi"]):
        st.write(f"- {item}")
else:
    st.write("Aucun matériau ajouté pour le moment.")


#import  as st

# Exemple de liste globale de matériaux avec leur épaisseur et leur conductivité
# Cette liste devrait être définie et mise à jour dans votre application
# Format de chaque élément : (nom_du_matériau, épaisseur, conductivité)
if "nom_mat_epai" not in st.session_state:
    st.session_state.nom_mat_epai = [
        ("Mortier de chaux", 0.1, 0.87),
        ("Carreaux de plâtre pleins .", 0.08, 1.4),
        ("Liège Comprimé", 0.05, 0.1)
    ]

st.subheader("Modifier l'épaisseur d'un matériau")

# Si la liste n'est pas vide, afficher la selectbox
if st.session_state.nom_mat_epai:
    # Préparer l'affichage de la liste
    material_names = [f"{m[0]} -- {m[1]} m" for m in st.session_state.nom_mat_epai]
    selected_index = st.selectbox(
        "Sélectionnez un matériau à modifier",
        range(len(st.session_state.nom_mat_epai)),
        format_func=lambda i: material_names[i]
    )
    
    new_thickness = st.text_input("Nouvelle épaisseur (en m)", "")
    
    if st.button("Modifier l'épaisseur"):
        try:
            new_thickness_value = float(new_thickness)
            # Récupérer les données actuelles et mettre à jour la valeur
            material_name, _, conductivite = st.session_state.nom_mat_epai[selected_index]
            st.session_state.nom_mat_epai[selected_index] = (material_name, new_thickness_value, conductivite)
            st.success(f"L'épaisseur du matériau '{material_name}' a été mise à jour à {new_thickness_value} m.")
        except ValueError:
            st.error("L'épaisseur doit être un nombre.")
else:
    st.info("Aucun matériau n'est disponible pour modification.")

st.subheader("Supprimer un matériau")

if st.session_state.nom_mat_epai:
    # Préparer l'affichage de la liste pour suppression
    material_names = [f"{m[0]} -- {m[1]} m" for m in st.session_state.nom_mat_epai]
    del_index = st.selectbox(
        "Sélectionnez un matériau à supprimer",
        range(len(st.session_state.nom_mat_epai)),
        format_func=lambda i: material_names[i]
    )
    
    if st.button("Supprimer le matériau"):
        removed = st.session_state.nom_mat_epai.pop(del_index)
        st.success(f"Le matériau '{removed[0]}' a été supprimé.")
else:
    st.info("Aucun matériau à supprimer.")

# Affichage de la liste mise à jour pour vérification
st.subheader("Liste des matériaux sélectionnés")
if st.session_state.nom_mat_epai:
    st.write(st.session_state.nom_mat_epai)
else:
    st.write("La liste est vide.")


# fonction pour ajouter le paroi
def Ajouter_le_paroi():
    try:
        nom_de_paroi = entry_nom_paroi.get()

        if not nom_de_paroi:
            messagebox.showerror("erreur", "veuillez inserez le nom de  mur")
            return

        if nom_de_paroi in resistance_des_murs:
            messagebox.showerror("erreur", f"ce paroi '{nom_de_paroi}' est deja créé.")
            return
        # condition de position de mur et type de contacte
        if rd_paroi_en_contact.get() == 1:
            if rd_position_de_mur.get() == 1:
                h_interieur_hiver = 0.11
                h_exterieur_hiver = 0.06
                h_interieur_ete = 0.10
                h_exterieur_ete = 0.04
            elif rd_position_de_mur.get() == 2:
                h_interieur_hiver = 0.09
                h_exterieur_hiver = 0.05
                h_interieur_ete = 0.16
                h_exterieur_ete = 0.04
            elif rd_position_de_mur.get() == 3:
                h_interieur_hiver = 0.17
                h_exterieur_hiver = 0.05
                h_interieur_ete = 0.08
                h_exterieur_ete = 0.04
            else:
                messagebox.showerror("erreur", "Indiquez si le mur est horizontal ou vertical.")
                return

        elif rd_paroi_en_contact.get() == 2:
            if rd_position_de_mur.get() == 1:
                h_interieur_hiver = 0.11
                h_exterieur_hiver = 0.11
                h_interieur_ete = 0.10
                h_exterieur_ete = 0.11
            elif rd_position_de_mur.get() == 2:
                h_interieur_hiver = 0.09
                h_exterieur_hiver = 0.09
                h_interieur_ete = 0.17
                h_exterieur_ete = 0.17
            elif rd_position_de_mur.get() == 3:
                h_interieur_hiver = 0.17
                h_exterieur_hiver = 0.17
                h_interieur_ete = 0.08
                h_exterieur_ete = 0.09
            else:
                messagebox.showerror("erreur", "Indiquez si le mur est horizontal ou vertical.")
                return
        else:
            messagebox.showerror("erreur", "Indiquez le contacte de Paroi.")
            return

        resistance_total = 0
        poid_total = 0
        for mater_name, epaisseur in nom_mat_epai:
            materiel = materiaux[mater_name]
            conductivite = materiel["conductivite"]
            masse_volum = materiel["masse volumique"]
            resistance = epaisseur / conductivite
            poid = masse_volum * epaisseur
            print(resistance)
            resistance_total += resistance
            poid_total += poid

        print("r de mat est : ", resistance_total)
        nom_mat_epai.clear()
        resistance_total_he_hiver = resistance_total + (h_exterieur_hiver + h_interieur_hiver)
        resistance_total_he_ete = resistance_total + (h_exterieur_ete + h_interieur_ete)
        print("r total est : ", resistance_total_he_hiver)
        resistance_des_murs[nom_de_paroi] = (resistance_total_he_hiver, poid_total)
        coefficient_de_transmission_hiver = 1 / resistance_total_he_hiver

        resi = f"{coefficient_de_transmission_hiver:.3f}"
        poi = f"{poid:.3f}"
        tree_paroi_ajout.insert("", "end", values=(nom_de_paroi, resi, poi))
        cmbol_nord.configure(values=list(resistance_des_murs.keys()))
        cmbol_sud.configure(values=list(resistance_des_murs.keys()))
        cmbol_Est.configure(values=list(resistance_des_murs.keys()))
        cmbol_Ouest.configure(values=list(resistance_des_murs.keys()))
     #   cmbol_Nord_Ouest.configure(values=list(resistance_des_murs.keys()))
        cmbol_Nord_Est.configure(values=list(resistance_des_murs.keys()))
        cmbol_Sud_Est.configure(values=list(resistance_des_murs.keys()))
        cmbol_Sud_Ouest.configure(values=list(resistance_des_murs.keys()))
        cmbol_Plancher_bas.configure(values=list(resistance_des_murs.keys()))
        cmbol_Plancher_Terrasse.configure(values=list(resistance_des_murs.keys()))
        cmbol_local_non_chauffé.configure(values=list(resistance_des_murs.keys()))
        lis_de_mat_choisi.delete(0, END)
        rd_paroi_en_contact.set(0)
        rd_position_de_mur.set(0)
        entry_nom_paroi.delete(0, END)

    except ValueError:
        print("erreur")

    for nompar in resistance_des_murs:
        print(f"{nompar},leur resistance est :{resistance_total_he_hiver:.3f}")

#import streamlit as st

# -------------------------
# Fonctions pour la logique métier
# -------------------------

def afficher_coefficients():
    # Remplacez cette fonction par votre logique d'affichage des coefficients
    st.write("Affichage des coefficients... (fonction à adapter)")

def transferer_informations():
    # Remplacez cette fonction par votre logique de transfert des informations
    st.write("Transfert des informations... (fonction à adapter)")

def verification_page_1(altitude, latitude, type_bati):
    if altitude is None or altitude <= 0:
        st.error("SVP, entrez une altitude positive.")
        return False
    if latitude is None or latitude <= 0:
        st.error("SVP, entrez une latitude positive.")
        return False
    if not type_bati or type_bati == "":
        st.error("SVP, choisissez le type de bâtiment.")
        return False
    return True

# -------------------------
# Partie "Page 1" : Vérification des données
# -------------------------

st.header("Vérification des données")
altitude = st.number_input("Altitude (m)", min_value=0.0, format="%.2f")
latitude = st.number_input("Latitude (°)", min_value=0.0, format="%.2f")
type_bati = st.selectbox("Type de bâtiment", ["", "Logement individuel", "Logement collectif"])

if st.button("Valider et passer à la page suivante"):
    if verification_page_1(altitude, latitude, type_bati):
        afficher_coefficients()
        transferer_informations()
        st.success("Vérification réussie, passage à la page suivante!")
        # Vous pouvez utiliser une variable de session pour contrôler la navigation
        st.session_state.page = "Page 2"

# -------------------------
# Partie : Suppression d'une paroi
# -------------------------

st.header("Supprimer une paroi")

# On stocke le dictionnaire des parois dans st.session_state pour conserver son état
if "resistance_des_murs" not in st.session_state:
    # Exemple de données initiales
    st.session_state.resistance_des_murs = {
        "Mur A": (1.5, 200),
        "Mur B": (2.0, 250)
    }

if st.session_state.resistance_des_murs:
    paroi_names = list(st.session_state.resistance_des_murs.keys())
    selected_paroi = st.selectbox("Sélectionnez une paroi à supprimer", paroi_names)
    if st.button("Supprimer la paroi"):
        del st.session_state.resistance_des_murs[selected_paroi]
        st.success(f"La paroi '{selected_paroi}' a été supprimée.")
        st.write("Mise à jour des parois:", st.session_state.resistance_des_murs)
else:
    st.info("Aucune paroi à supprimer.")



#import streamlit as st

# Dictionnaire complet des wilayas
wilaya = {
    "1-ADRAR": {
        "Groupe 1: TINERKOUK, BORDJ BADJI MOKHTAR": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "D"
    },
    "2-CHLEF": {
        "Groupe 1: TENES, OUED GHOUSSINE, SIDI ABDERRAHMANE, SIDI AKKACHA": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "3-LAGHOUAT": {
        "Groupe 1: SIDI MAKHLOUF, EL ASSAFIA, LAGHOUAT, AIN MADHI, KSAR EL HIRANE, MEKHAREG, KHENEG, HASSI DHELAA, EL HAOUAITA, HASSI RMEL": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "4-OUM EL BOUAGH": {
        "Toutes les communes": "B"
    },
    "5-BATNA": {
        "Groupe 1: METKAOUAK, OULED AMMAR, BARI KA, TILATOU, SEGGANA, BITAM, MDOUKAL, TIGHARGHAR": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "6-BEJAIA": {
        "Groupe 1: BENI KSILA, TOUDJA, BEJAIA, EL KSEUR, TAOURIRT IGHIL, OUED GHIR, TALA HAMZA": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "7-BISKRA": {
        "Groupe 1: KHAN GAT SIDI NADJI": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "C"
    },
    "8-BECHAR": {
        "Groupe 1: BENI OUNIF, MOUGHEUL, BOUKAIS, BECHAR, LAHMAR, KENADSA, MERIDJA, TAGHIT, ERG FERRADJ, ABADLA": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "D"
    },
    "9-BLIDA": {
        "Toutes les communes": "A"
    },
    "10-BOUIRA": {
        "Groupe 1: MEZDOUR, BORDJ OUKHRISS, RIDANE, DIRAH, MAAMORA, TAGUEDIT, HADJERA ZERGA": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "11-TAMANRASSET": {
        "Groupe 1: TAZROUK, TAMANRASSET, ABALESSA, TIN ZAOUA TINE, IN GUEZZAM": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "D"
    },
    "12-TEBESSA": {
        "Groupe 1: FERKANE, NEGRINE": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "13-TLEMCEN": {
        "Groupe 1: AIN TALLOUT, OULED MIMOUN, OUED CHOULY, BENI SEMIEL, TERNI BENI HEDIEL, AIN GHORABA, BENI BOUSSAID, BENI BAHDEL, BENI SNOUS, SEBDOU, AZAILS, EL GOR, SIDI DJILLALI, EL ARICHA, EL BOUIHI": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "14-TIARET": {
        "Toutes les communes": "B"
    },
    "15-TIZIOUZOU": {
        "Groupe 1: MIZRANA": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "16-ALGER": {
        "Toutes les communes": "A"
    },
    "17-DJELFA": {
        "Groupe 1: BENHAR, AIN OUESSARA, BIRINE, AIN FEKKA, EL KHEMIS, HASSI FDOUL, HAD SAHARY, SIDI LAADJEL, BOUIRA LAHDAB, GUERNINI, HASSI EL EUCH, HASSI BAHBAH, ZAAFRANE, EL GUEDDID, CHAREF, BENI YAGOUB, EL IDRISSIA, DOUIS, AIN CHOUHADA": "B",
        "Groupe 2: OUM LAADHAM, GUETTARA": "D",
        "Groupe 3: Toutes les communes autres que celles figurant aux groupes de communes 1 et 2": "C"
    },
    "18-JIJEL": {
        "Toutes les communes": "A"
    },
    "19-SETIF": {
        "Groupe 1: BABOR, AIT TIZI, MZADA, AIN SEBT, SERDJ EL GHOUL, OUED EL BARED, BENI MOUHLI, BOUANDAS, BENI AZIZ, BOUSSELAM, BENI CHEBANA, TALA IF ACENE, BENI OUARTILANE, TIZI NBECHAR, DRAA KEBILA, AIN LAGRADJ, MAOUKLANE, MAAOUIA, DEHAMCHA, AMOUCHA, AIN EL KEBIRA, DJEMILA, HAMMAM GUERGOUR, AIN ROUA, HARBIL, AIN ABESSA, BOUGAA, GUENZET TASSAMEURT, OULED ADDOUANE, BENI FOUDA, EL OURICIA, BENI HOCINE, TACHOUDA": "A",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "20-SAIDA": {
        "Toutes les communes": "B"
    },
    "21-SKIKDA": {
        "Groupe 1: AIN ZOUIT, FIL FILA, SKIKDA, HAMMADI KROUMA, EL HADAIEK": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "22-SIDI BEL ABBES": {
        "Groupe 1: MAKEDRA, AIN EL BERD, BOUDJEBAA EL BORDJ, AIN ADDEN, AIN THRID, SIDI HAMADOUCHE, TESSALA, ZEROUALA, SFISEF, IDI BRAHIM, SEHALA THAOURA, SIDI LAHCENE, SIDI BEL ABBES, MOSTEFA BEN BRAHIM, TILMOUNI, SIDI DAHO, SIDI YACOUB, AIN KADA, BELARBI, AMARNAS, SIDI KHALED, SIDI ALI BOUSSIDI, BOUKANEFIS, LAMTAR, HASSI ZAHANA, BEDRABINE EL MOKRANI": "A",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "23-ANNABA": {
        "Toutes les communes": "A"
    },
    "24-GUELMA": {
        "Groupe 1: HAMMAM NBAIL, OUED CHEHAM, KHEZARA, OUED ZENATE, DAHOUARA, AIN LARBI, AIN REGGADA, BOUHACHANA, AIN SANDEL, AIN MAKHLOUF, T AMLOUKA": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "25-CONSTANTINE": {
        "Groupe 1: EL KHROUB, AIN SMARA, AIN ABID, OULED RAHMOUN": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "26-MEDEA": {
        "Toutes les communes": "B"
    },
    "27-MOSTAGANEM": {
        "Toutes les communes": "A"
    },
    "28-MSILA": {
        "Groupe 1: HAMMAM DHALAA, BENI ILMENE, OUENOUGHA, SIDI AISSA, TARMOUNT, MAADID, BOUTI SAYEH, OULED ADDI GUEBALA, DEHAHNA, MAGRA, BERHOUM, BELAIBA": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "C"
    },
    "29-MASCARA": {
        "Groupe 1: MOCTADOUZ, EL GHOMRI, SIDI ABDELMOUMENE, ALAIMIA, RAS EL AIN AMIROUCHE, SEDJERARA, MOHAMMADIA, OGGAZ, BOUHENNI, EL MENAOUER, SIG, ZAHANA, EL BORDJ, AIN FARES, HACINE, EL MAMOUNIA, FERRAGUIG, SIDI A ABDELDJABAR, SEHAILI, CHORFA, EL GAADA, KHALOUIA, ELGUEITNA, TIGHENNIF, MAOUSSA, MASCARA, EL KEURT, TIZI, BOUHANIFIA": "A",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "30-OUARGLA": {
        "Groupe 1: EL BORMA": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "D"
    },
    "31-ORAN": {
        "Toutes les communes": "A"
    },
    "32-ELBAYADH": {
        "Groupe 1: BREZINA, EL ABIODH SIDI CHEIKH, EL BNOUD": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "33-ILLIZI": {
        "Toutes les communes": "C"
    },
    "34-BORDJ BOU ARRERIDJ": {
        "Groupe 1: EL MAIN, DJAAFRA, TAFREG, KHELIL, TESMART, BORDJ ZEMOURA, COLLA, OULED SIDI BRAHIM, OULED DAHMANE, THENIET EL ANSEUR, HARAZA": "A",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "35-BOUMERDES": {
        "Groupe 1: DELLYS, SIDI DAOUD, AFIR, BEN CHOUD, BAGHLIA, OULED AISSA, TAOURGA": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "36-EL-TARF": {
        "Groupe 1: EL KALA, BERRlHANE": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "37-TINDOUF": {
        "Toutes les communes": "D"
    },
    "38-TISSEMSILT": {
        "Groupe 1: LAZHARIA, LARBAA, BOUCAID, BORDJ A BOUNAAMA": "A",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "39-EL OUED": {
        "Groupe 1: OUM TIOUR, EL MGHAIR, SIDI KHELLIL, TENDLA, MRARA, DJAMAA, SIDI AMRANE": "D",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "C"
    },
    "40-KHENCHELA": {
        "Groupe 1: BABAR": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "41-SOUK-AHRAS": {
        "Groupe 1: MECHROHA, AIN ZANA, OULED DRISS": "A",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    },
    "42-TIPAZA": {
        "Toutes les communes": "A"
    },
    "43-MILA": {
        "Groupe 1: OUED ATHMANIA, BENYAHIA ABDERRAHMANE, OUED SEGUEN, CHELGHOUM LAID, TADJENANET, TELAGHMA, EL MCHIRA, OULED KHELLOUF": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "44-AIN-DEFLA": {
        "Toutes les communes": "A"
    },
    "45-NAAMA": {
        "Toutes les communes": "B"
    },
    "46-AIN TEMOUCHENT": {
        "Groupe 1: SIDI SAFI, BENI SAF, OULHACA GHERRABA, AIN AL TOLBA, EL EMIR ABDELKADER": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "47-GHARDAIA": {
        "Groupe 1: EL GUERRARA, ZELFANA": "D",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "C"
    },
    "48-RELIZANE": {
        "Groupe 1: OUED ESSALEM": "B",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    }
}

# Exemple d'utilisation en Streamlit
st.header("Sélectionnez votre Wilaya et Groupe de Communes")

selected_wilaya = st.selectbox("Sélectionnez une Wilaya", list(wilaya.keys()))
groupes = list(wilaya[selected_wilaya].keys())
selected_groupe = st.selectbox("Sélectionnez un Groupe de Communes", groupes)

zone = wilaya[selected_wilaya][selected_groupe]
st.write(f"La zone climatique correspondante est : **{zone}**")



#import streamlit as st

st.title("Information de Projet")

# --- Sélection de la Wilaya, du Groupe de Communes et affichage de la zone climatique ---

# Exemple de dictionnaire des wilayas (vous pouvez ajouter ou modifier selon vos besoins)
wilaya = {
    "1-ADRAR": {
        "Groupe 1: TINERKOUK, BORDJ BADJI MOKHTAR": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "D"
    },
    "2-CHLEF": {
        "Groupe 1: TENES, OUED GHOUSSINE, SIDI ABDERRAHMANE, SIDI AKKACHA": "A1",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "A"
    },
    "3-LAGHOUAT": {
        "Groupe 1: SIDI MAKHLOUF, EL ASSAFIA, LAGHOUAT, AIN MADHI, KSAR EL HIRANE, MEKHAREG, KHENEG, HASSI DHELAA, EL HAOUAITA, HASSI RMEL": "C",
        "Groupe 2: Toutes les communes autres que celles figurant aux groupes de communes 1": "B"
    }
    # Vous pouvez compléter avec d'autres wilayas...
}

selected_wilaya = st.selectbox("Sélectionnez la Wilaya", list(wilaya.keys()))
groupes = list(wilaya[selected_wilaya].keys())
selected_groupe = st.selectbox("Sélectionnez le Groupe de Communes", groupes)

zone = wilaya[selected_wilaya][selected_groupe]
st.write(f"Zone climatique : **{zone}**")

# --- Sélection du type de logement ---

type_bati = st.selectbox(
    "Type de logement",
    ["Logement individuel", "Logement en immeubles collectifs, bureaux, locaux à usage d'hébergement"]
)

# --- Fonction pour obtenir les coefficients de référence ---

def get_coefficients_de_reference(zone, type_logement):
    coefficients = {
        ("B", "C", "Logement individuel"): (0.9, 2, 1, 3, 3.8),
        ("A", "A1", "D", "Logement individuel"): (0.9, 2, 1.2, 3, 3.8),
        ("B", "C", "Logement en immeubles collectifs, bureaux, locaux à usage d'hébergement"): (0.75, 2, 1, 3, 3.8),
        ("A", "A1", "D", "Logement en immeubles collectifs, bureaux, locaux à usage d'hébergement"): (0.9, 2, 1.2, 3, 3.8),
    }
    for key, value in coefficients.items():
        # On vérifie si la zone est présente dans le tuple key et que le type de logement correspond au dernier élément.
        if zone in key and type_logement == key[-1]:
            return value
    return None

# --- Affichage des coefficients ---
if st.button("Afficher les coefficients"):
    coeffs = get_coefficients_de_reference(zone, type_bati)
    if coeffs:
        a, b, c, d, e = coeffs
        somme = a + b + c + d + e
        st.write(f"a = {a}")
        st.write(f"b = {b}")
        st.write(f"c = {c}")
        st.write(f"d = {d}")
        st.write(f"e = {e}")
        st.write(f"Somme = {somme}")
    else:
        st.write("Valeurs non définies")

#import streamlit as st

st.header("Information de Projet")

# Nom du projet
nom_projet = st.text_input("Nom du Projet")

# Wilaya
# On suppose que le dictionnaire 'wilaya' est déjà défini (cf. code précédent)
selected_wilaya = st.selectbox("Wilaya", list(wilaya.keys()))

# Groupe de Communes
groupes = list(wilaya[selected_wilaya].keys()) if selected_wilaya in wilaya else []
selected_groupe = st.selectbox("Groupe de Communes", groupes)

# Zone climatique (affichage automatique)
zone_climatique = wilaya[selected_wilaya][selected_groupe] if selected_wilaya in wilaya and selected_groupe in wilaya[selected_wilaya] else ""
st.text_input("Zone Climatique", value=zone_climatique, disabled=True)

# Altitude
altitude = st.number_input("Altitude (m)", min_value=0.0, step=0.1)

# Latitude
latitude = st.number_input("Latitude (°)", min_value=0.0, step=0.1)

# Type de logement
type_bati = st.selectbox(
    "Type de logement",
    ["", "Logement individuel", "Logement en immeubles collectifs, bureaux, locaux à usage d'hébergement"]
)

# Bouton Suivant
if st.button("Suivant"):
    # Vous pouvez sauvegarder ces informations dans st.session_state ou passer à une autre "page"
    st.session_state.nom_projet = nom_projet
    st.session_state.wilaya = selected_wilaya
    st.session_state.groupe = selected_groupe
    st.session_state.zone_climatique = zone_climatique
    st.session_state.altitude = altitude
    st.session_state.latitude = latitude
    st.session_state.type_bati = type_bati
    st.success("Informations sauvegardées. Passez à la page suivante.")

#import streamlit as st
#import pandas as pd

st.header("Ajouter des parois")

# Saisie du nom de paroi
nom_paroi = st.text_input("Nom de Paroi", placeholder="Entrez le nom de la paroi")

# Choix de la position du mur
position_options = [
    "Lateral (Mur) α>60",
    "Ascendant (Toiture): α<=60",
    "Descendant (Plancher)"
]
position = st.radio("Position", options=position_options)

# Choix du contact de la paroi
contact_options = [
    "Exterieur / Passage Ouvert / Local Ouvert",
    "Local Chauffé ou non Chauffé / Comble / Vide Sanitaire"
]
contact = st.radio("En contact avec", options=contact_options)

st.markdown("---")
st.subheader("Recherche de matériaux")

# Champ de recherche pour filtrer les matériaux
recherche = st.text_input("Recherche", placeholder="Tapez pour rechercher un matériau")

# Exemple de dictionnaire de matériaux (à compléter selon vos données)
materiaux = {
    "Mortier de chaux": {"conductivite": 0.87, "masse volumique": 1800},
    "Carreaux de plâtre pleins": {"conductivite": 1.4, "masse volumique": 950},
    "Liège Comprimé": {"conductivite": 0.1, "masse volumique": 500},
    "Expansé pur": {"conductivite": 0.044, "masse volumique": 130},
    "Verre": {"conductivite": 0.80, "masse volumique": 1900},
    "Crépis": {"conductivite": 0.84, "masse volumique": 3800},
    # Ajoutez d'autres matériaux au besoin...
}

# Fonction de filtrage des matériaux
def filter_materiaux(search_text, data):
    if not search_text:
        return data
    return {k: v for k, v in data.items() if search_text.lower() in k.lower()}

filtered_materiaux = filter_materiaux(recherche, materiaux)

# Conversion du dictionnaire en DataFrame pour affichage
def dict_to_df(data):
    rows = []
    for key, val in data.items():
        rows.append({
            "Matériaux": key,
            "Conductivité (W/m.K)": val["conductivite"],
            "Masse Volumique (kg/m³)": val["masse volumique"]
        })
    return pd.DataFrame(rows)

df_materiaux = dict_to_df(filtered_materiaux)

st.dataframe(df_materiaux, use_container_width=True)

# Optionnel : Permettre de sélectionner un matériau parmi ceux affichés
if filtered_materiaux:
    selected_material = st.selectbox("Sélectionnez un matériau", list(filtered_materiaux.keys()))
    st.info(f"Matériau sélectionné : {selected_material}")


#import streamlit as st
#import pandas as pd

st.header("Gestion des Matériaux et Parois")

# --- Saisie de l'épaisseur et sélection du matériau ---
# On simule ici la sélection d'un matériau (à adapter selon votre contexte)
selected_material = st.selectbox("Sélectionnez un matériau", 
                                 options=["Mortier de chaux", "Carreaux de plâtre", "Liège Comprimé"])
thickness = st.number_input("Entrez l'épaisseur (m)", min_value=0.0, format="%.2f", value=0.0)

# Initialisation de la liste des matériaux sélectionnés dans la session
if "selected_materials" not in st.session_state:
    st.session_state.selected_materials = []

# Bouton pour ajouter le matériau avec son épaisseur
if st.button("Ajouter le matériau"):
    if selected_material and thickness > 0:
        st.session_state.selected_materials.append({
            "Matériau": selected_material, 
            "Épaisseur (m)": thickness
        })
        st.success(f"{selected_material} ajouté avec une épaisseur de {thickness} m")
    else:
        st.error("Veuillez sélectionner un matériau et saisir une épaisseur valide.")

# --- Affichage et modification de la liste des matériaux ---
st.subheader("Matériaux sélectionnés")
if st.session_state.selected_materials:
    df_materials = pd.DataFrame(st.session_state.selected_materials)
    st.dataframe(df_materials, use_container_width=True)
    
    # Modification : choix de l'indice du matériau à modifier et saisie de la nouvelle épaisseur
    index_to_modify = st.number_input("Indice du matériau à modifier (0-indexé)", 
                                      min_value=0, max_value=len(st.session_state.selected_materials)-1, step=1)
    new_thickness = st.number_input("Nouvelle épaisseur (m)", min_value=0.0, format="%.2f", value=0.0, key="mod_thickness")
    if st.button("Modifier l'épaisseur"):
        if new_thickness > 0:
            st.session_state.selected_materials[index_to_modify]["Épaisseur (m)"] = new_thickness
            st.success("Épaisseur modifiée.")
        else:
            st.error("Veuillez saisir une nouvelle épaisseur valide.")
    
    # Suppression : choix de l'indice du matériau à supprimer
    index_to_delete = st.number_input("Indice du matériau à supprimer (0-indexé)", 
                                      min_value=0, max_value=len(st.session_state.selected_materials)-1, step=1, key="del_index")
    if st.button("Supprimer le matériau"):
        deleted = st.session_state.selected_materials.pop(index_to_delete)
        st.success(f"{deleted['Matériau']} supprimé.")
        st.experimental_rerun()
else:
    st.info("Aucun matériau n'a encore été ajouté.")

# --- Gestion des parois ---
st.markdown("---")
st.subheader("Parois")

# Bouton pour calculer/ajouter une paroi (simulation)
if "parois" not in st.session_state:
    st.session_state.parois = []

if st.button("Ajouter le Paroi"):
    # Ici, vous appelez votre fonction de calcul de résistance de paroi (ex: Ajouter_le_paroi)
    # On simule l'ajout d'une paroi avec des valeurs d'exemple
    st.session_state.parois.append({
        "Mur": "Paroi Exemple",
        "Coefficient de Transmission (W/°C.m²)": 1.23,
        "Masse Surfacique (kg/m²)": 150
    })
    st.success("Paroi ajoutée.")

# Affichage des parois créées
if st.session_state.parois:
    df_parois = pd.DataFrame(st.session_state.parois)
    st.dataframe(df_parois, use_container_width=True)
else:
    st.info("Aucune paroi créée pour le moment.")


#import streamlit as st

def sup_parois():
    st.write("Paroi supprimée (exemple).")
    # Logique réelle pour supprimer la paroi

def verification_page_2():
    st.write("Vérification de la page 2 (exemple).")
    # Logique réelle de vérification

# On simule une variable de navigation
if "page" not in st.session_state:
    st.session_state.page = "page1"
# Bouton pour supprimer la paroi créée
if st.button("Supprimer le Paroi"):
    sup_parois()  # Assurez-vous que cette fonction est adaptée pour Streamlit

# Bouton pour revenir à la page 1 (navigation via st.session_state par exemple)
if st.button("Retour"):
    st.session_state.page = "page1"  # Exemple de gestion de navigation
    st.experimental_rerun()
# Bouton pour passer à la page 3 (après vérification)
#if st.button("Suivant"):
    verification_page_2()  # Assurez-vous que cette fonction est adaptée pour Streamlit
    st.write("Aller vers la page 3.")
st.header("Configuration de la paroi Nord")

# Choix de l'orientation du mur nord
var_nord = st.radio(
    "Le mur est-il orienté vers le nord ?",
    options=[1, 2],
    format_func=lambda x: "Oui" if x == 1 else "Non"
)

if var_nord == 1:
    st.subheader("Configuration Homogénéité du Mur")
    var_homogene_oui_nord = st.radio(
        "Votre mur est-il homogène ?",
        options=[1, 2],
        format_func=lambda x: "Oui" if x == 1 else "Non"
    )
    
    if var_homogene_oui_nord == 1:
        st.write("Configuration pour mur homogène")
        # Saisie de la surface du mur
        surface_nord = st.number_input("Surface du mur (m²)", min_value=0.0, value=0.0)
        
        # Simulation d'une sélection de paroi parmi des données enregistrées
        # Ici, nous utilisons st.session_state pour stocker un exemple de données de parois
        if "resistance_des_murs" not in st.session_state:
            st.session_state.resistance_des_murs = {"Mur Exemple": (1.5, 200)}  # (résistance, masse)
        
        paroi_options = list(st.session_state.resistance_des_murs.keys())
        paroi_choisi_nord = st.selectbox("Sélectionnez la paroi", paroi_options)
        
        if surface_nord > 0 and paroi_choisi_nord:
            resistance_de_paroi, masse_paroi = st.session_state.resistance_des_murs[paroi_choisi_nord]
            coef_k_nord = 1 / resistance_de_paroi if resistance_de_paroi != 0 else 0
            dep_paroi_nord = surface_nord * coef_k_nord
            st.write(f"Déperdition de paroi (Nord) calculée : **{dep_paroi_nord:.3f}**")
    
    elif var_homogene_oui_nord == 2:
        st.write("Configuration pour mur non homogène")
        # Saisie de la surface de la fenêtre et du mur
        surface_fenetre = st.number_input("Surface totale des fenêtres (m²)", min_value=0.0, value=0.0)
        surface_mur = st.number_input("Surface du mur (m²)", min_value=0.0, value=0.0)
        # Saisie supplémentaire pour type de fenêtre, matériaux, etc. peut être ajoutée ici
        st.write("Calcul de la déperdition pour un mur non homogène à intégrer ici.")
else:
    st.write("Aucun mur nord sélectionné. La configuration de la paroi nord est ignorée.")


#import streamlit as st

def calcul_dep_fenetre_nord():
    # Sélection du type de fenêtre
    choix_fenetre_nord = st.selectbox(
        "Choisissez le type de fenêtre",
        options=["Simple", "Double", "Fenetre double"]
    )
    
    # Sélection du matériau de la fenêtre
    chois_materiaux_fenetre_nord = st.selectbox(
        "Choisissez le matériau de la fenêtre",
        options=["Bois", "Autre"]
    )
    
    # Saisie de la surface de la fenêtre en m²
    surface_fenetre_nord = st.number_input(
        "Surface de la fenêtre (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    # Pour le cas "Double", demande la sélection de l'épaisseur
    choix_eppaisseur_nord = None
    if choix_fenetre_nord == "Double":
        choix_eppaisseur_nord = st.selectbox(
            "Choisissez l'épaisseur (pour fenêtre double)",
            options=["5 à 7 ", "8 à 9", "10 à 11", "12 à 13"]
        )
    
    st.write("Type de fenêtre sélectionné :", choix_fenetre_nord)
    
    # Calcul de kwin_nord selon les choix
    if choix_fenetre_nord == "Simple":
        st.write("Vous avez choisi simple")
        if chois_materiaux_fenetre_nord == "Bois":
            kwin_nord = 5
        else:
            kwin_nord = 5.8
    elif choix_fenetre_nord == "Double":
        st.write("Vous avez choisi double")
        if chois_materiaux_fenetre_nord == "Bois":
            if choix_eppaisseur_nord == "5 à 7 ":
                kwin_nord = 3.3
            elif choix_eppaisseur_nord == "8 à 9":
                kwin_nord = 3.1
            elif choix_eppaisseur_nord == "10 à 11":
                kwin_nord = 3
            elif choix_eppaisseur_nord == "12 à 13":
                kwin_nord = 2.9
        else:
            if choix_eppaisseur_nord == "5 à 7 ":
                kwin_nord = 4
            elif choix_eppaisseur_nord == "8 à 9":
                kwin_nord = 3.9
            elif choix_eppaisseur_nord == "10 à 11":
                kwin_nord = 3.8
            elif choix_eppaisseur_nord == "12 à 13":
                kwin_nord = 3.7
    elif choix_fenetre_nord == "Fenetre double":
        if chois_materiaux_fenetre_nord == "Bois":
            kwin_nord = 2.6
        else:
            kwin_nord = 3

    st.write("kwin_nord =", kwin_nord)
    
    # Calcul de la résistance totale r et de la déperdition
    r = (1 / kwin_nord) + 0.025 + 0.03 + 0.16
    dep_fenetre_nord = surface_fenetre_nord * (1 / r)
    
    return dep_fenetre_nord

# Bouton pour lancer le calcul et afficher le résultat
if st.button("Calculer déperdition de la fenêtre nord"):
    dep = calcul_dep_fenetre_nord()
    st.write(f"Déperdition de la fenêtre nord : {dep:.3f}")


#import streamlit as st

def port_nord():
    # Sélection du type de contact
    choix_contact = st.selectbox(
        "Choisissez le type de contact du port",
        options=["Exterieur", "Local Non Chauffé"]
    )
    
    # Sélection du type de porte
    choix_port = st.selectbox(
        "Choisissez le type de porte",
        options=[
            "Portes Opaques en Bois", 
            "Portes Opaques en Metal", 
            "Portes en Bois avec une proportion de vitrage <30%",
            "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
            "Portes en Metal equipées de vitrage simple"
        ]
    )
    
    # Saisie de la surface du port en m²
    surface_port = st.number_input("Surface du port (m²)", min_value=0.0, value=0.0, step=0.1)
    
    # Détermination de k_port_nord en fonction des choix
    if choix_contact == "Exterieur":
        if choix_port == "Portes Opaques en Bois":
            k_port_nord = 3.5
        elif choix_port == "Portes Opaques en Metal":
            k_port_nord = 5.8
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port_nord = 4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port_nord = 4.5
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port_nord = 5.8
    elif choix_contact == "Local Non Chauffé":
        if choix_port == "Portes Opaques en Bois":
            k_port_nord = 2
        elif choix_port == "Portes Opaques en Metal":
            k_port_nord = 4.5
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port_nord = 2.4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port_nord = 2.7
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port_nord = 4.5
    
    st.write("k_port_nord =", k_port_nord)
    
    # Calcul de la déperdition
    dep_port_nord = surface_port * k_port_nord
    return dep_port_nord

# Bouton pour lancer le calcul et afficher le résultat
if st.button("Calculer déperdition du port nord"):
    dep = port_nord()
    st.write(f"Déperdition du port nord : {dep:.3f}")



#import streamlit as st

st.markdown("## Entrée des Surfaces et Matériaux")
st.markdown("### Nord")

def calcul_dep_transmission_nord():
    # Sélection : le mur est-il orienté vers le nord ?
    var_nord = st.radio(
        "Le mur est-il orienté vers le nord ?",
        options=[1, 2],
        index=0,
        format_func=lambda x: "Oui" if x == 1 else "Non"
    )
    
    if var_nord == 1:
        # Saisie de la déperdition de la paroi nord (exemple ou calcul préalablement réalisé)
        dep_paroi_nord = st.number_input(
            "Déperdition de la paroi nord (W)",
            min_value=0.0, value=0.0, step=0.1
        )
        
        # Vérifier l'homogénéité du mur
        var_homogene = st.radio(
            "Le mur est-il homogène ?",
            options=[1, 2],
            index=0,
            format_func=lambda x: "Oui" if x == 1 else "Non"
        )
        
        if var_homogene == 1:
            dep_fenetre_nord = 0
            dep_port_nord = 0
            surface_fenetre_nord = 0
            surface_port_nord = 0
            surface_nord = st.number_input(
                "Surface du mur nord (m²)",
                min_value=0.0, value=0.0, step=0.1
            )
        else:
            dep_fenetre_nord = st.number_input(
                "Déperdition fenêtre nord (W)",
                min_value=0.0, value=0.0, step=0.1
            )
            dep_port_nord = st.number_input(
                "Déperdition port nord (W)",
                min_value=0.0, value=0.0, step=0.1
            )
            surface_nord = st.number_input(
                "Surface du mur nord (m²)",
                min_value=0.0, value=0.0, step=0.1
            )
            surface_fenetre_nord = st.number_input(
                "Surface des fenêtres nord (m²)",
                min_value=0.0, value=0.0, step=0.1
            )
            surface_port_nord = st.number_input(
                "Surface du port nord (m²)",
                min_value=0.0, value=0.0, step=0.1
            )
        
        total_surface = surface_nord + surface_fenetre_nord + surface_port_nord
        if total_surface > 0:
            dep_transmission_nord = ((dep_paroi_nord + dep_fenetre_nord + dep_port_nord) / total_surface) * surface_nord
        else:
            dep_transmission_nord = 0
        
        st.write(f"Déperdition transmission nord : **{dep_transmission_nord:.3f}**")
        return dep_transmission_nord
    else:
        st.write("Pas de mur nord sélectionné, déperdition transmission nord : **0**")
        return 0

# Appel de la fonction pour calculer et afficher la déperdition
calcul_dep_transmission_nord()

# Mise en page pour la section "Nord" (simulation des frames internes)
st.markdown("---")
st.markdown("### Configuration détaillée - Nord")
st.info("Ici, vous pouvez ajouter d'autres réglages ou informations concernant la configuration du mur nord, similaire aux frames internes dans Tkinter.")


#import streamlit as st

st.subheader("Configuration du mur nord")

# On simule ici une variable contenant les parois déjà créées.
# Par exemple, st.session_state.resistance_des_murs est un dictionnaire où la clé est le nom du mur.
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Exemple 1": (1.5, 200),
        "Mur Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur = st.selectbox(
    "Sélectionnez le mur",
    options=list(st.session_state.resistance_des_murs.keys())
)

# Question sur l'orientation du mur nord
mur_nord = st.radio(
    "Y a-t-il un mur orienté vers le nord ?",
    options=["Oui", "Non"]
)

# Question sur l'homogénéité du mur
mur_homogene = st.radio(
    "Votre mur est-il Homogène ?",
    options=["Oui", "Non"]
)

# Affichage d'un message de confirmation en fonction du choix d'homogénéité
if mur_homogene == "Oui":
    st.info("Configuration pour mur homogène sélectionnée")
else:
    st.info("Configuration pour mur non homogène sélectionnée")


#import streamlit as st

st.markdown("## Configuration de la partie Nord")

# Orientation du mur vers le nord (oui/non)
var_nord = st.radio(
    "Le mur est-il orienté vers le nord ?",
    options=["Oui", "Non"],
    index=0
)

# Section pour la configuration des surfaces et options de fenêtres
st.markdown("### Informations sur les surfaces et fenêtres")

# Saisie de la surface totale des fenêtres (en m²)
surface_fenetre_nord = st.number_input(
    "Surface totale des fenêtres (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Saisie de la surface totale du mur (en m²)
surface_mur_nord = st.number_input(
    "Surface totale du mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de fenêtre
type_fenetre_nord = st.selectbox(
    "Type de fenêtre",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)

# Pour le cas "Double", demander l'épaisseur (mm)
epaisseur_aim_dair_nord = None
if type_fenetre_nord == "Double":
    epaisseur_aim_dair_nord = st.selectbox(
        "Épaisseur (mm) pour fenêtre double",
        options=["sélectionner", "5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"],
        index=0
)

# Sélection du matériau de la fenêtre
materiaux_fenetre_nord = st.selectbox(
    "Matériaux de fenêtre",
    options=["sélectionner", "Bois", "Metal"],
    index=0
)

# Section pour le port nord (portes)
st.markdown("### Informations sur le port nord")

# Saisie de la surface totale des portes (en m²)
surface_port_exterieur_nord = st.number_input(
    "Surface totale des portes (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de contact du port
combo_type_contacte_port_exterieur_nord = st.selectbox(
    "Contact du port",
    options=["type", "Exterieur", "Local Non Chauffé"],
    index=0
)

# Sélection du matériau de la porte
combo_type_port_exterieur_nord = st.selectbox(
    "Matériau de la porte",
    options=[
        "type",
        "Portes Opaques en Bois",
        "Portes Opaques en Metal",
        "Portes en Bois avec une proportion de vitrage <30%",
        "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
        "Portes en Metal equipées de vitrage simple"
    ],
    index=0
)


#import streamlit as st

st.markdown("## Configuration de la partie Nord")

# Orientation du mur vers le nord (oui/non)
var_nord = st.radio(
    "Le mur est-il orienté vers le nord ?",
    options=["Oui", "Non"],
    index=0
)

# Section pour la configuration des surfaces et options de fenêtres
st.markdown("### Informations sur les surfaces et fenêtres")

# Saisie de la surface totale des fenêtres (en m²)
surface_fenetre_nord = st.number_input(
    "Surface totale des fenêtres (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Saisie de la surface totale du mur (en m²)
surface_mur_nord = st.number_input(
    "Surface totale du mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de fenêtre
type_fenetre_nord = st.selectbox(
    "Type de fenêtre",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)

# Pour le cas "Double", demander l'épaisseur (mm)
epaisseur_aim_dair_nord = None
if type_fenetre_nord == "Double":
    epaisseur_aim_dair_nord = st.selectbox(
        "Épaisseur (mm) pour fenêtre double",
        options=["sélectionner", "5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"],
        index=0
    )

# Sélection du matériau de la fenêtre
materiaux_fenetre_nord = st.selectbox(
    "Matériaux de fenêtre",
    options=["sélectionner", "Bois", "Metal"],
    index=0
)

# Section pour le port nord (portes)
st.markdown("### Informations sur le port nord")

# Saisie de la surface totale des portes (en m²)
surface_port_exterieur_nord = st.number_input(
    "Surface totale des portes (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de contact du port
combo_type_contacte_port_exterieur_nord = st.selectbox(
    "Contact du port",
    options=["type", "Exterieur", "Local Non Chauffé"],
    index=0
)

# Sélection du matériau de la porte
combo_type_port_exterieur_nord = st.selectbox(
    "Matériau de la porte",
    options=[
        "type",
        "Portes Opaques en Bois",
        "Portes Opaques en Metal",
        "Portes en Bois avec une proportion de vitrage <30%",
        "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
        "Portes en Metal equipées de vitrage simple"
    ],
    index=0
)


#import streamlit as st

st.markdown("## Configuration du mur Sud")

# Simulation des murs déjà créés (à adapter selon votre contexte)
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Exemple Sud 1": (1.5, 200),
        "Mur Exemple Sud 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur_sud = st.selectbox(
    "Choisissez le mur",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)

# Question sur l'orientation du mur sud
orientation_sud = st.radio(
    "Y a-t-il un mur orienté vers le sud ?",
    options=["Oui", "Non"],
    index=0
)

# Question sur l'homogénéité du mur
homogene_sud = st.radio(
    "Votre mur est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)

# Affichage d'un message selon la réponse sur l'homogénéité
if homogene_sud == "Oui":
    st.info("Configuration pour mur homogène sélectionnée")
else:
    st.info("Configuration pour mur non homogène sélectionnée")

# Radiobutton pour l'orientation vers sud (redondant ou complémentaire, selon le besoin)
orientation_radio_sud = st.radio(
    "Orientation du mur vers le sud",
    options=["Oui", "Non"],
    index=0
)

#import streamlit as st

st.markdown("## Configuration Fenêtre et Port - Sud")

st.markdown("### Fenêtre")

# Saisie de la surface totale de fenêtre (en m²)
surface_fenetre_sud = st.number_input(
    "Surface totale de fenêtre (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Saisie de la surface totale du mur (en m²)
surface_mur_sud = st.number_input(
    "Surface totale de mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de fenêtre
type_fenetre_sud = st.selectbox(
    "Type de fenêtre",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)

# Pour le cas "Double", demander l'épaisseur (mm)
epaisseur_aim_dair_sud = None
if type_fenetre_sud == "Double":
    epaisseur_aim_dair_sud = st.selectbox(
        "Épaisseur (mm) pour fenêtre double",
        options=["sélectionner", "5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"],
        index=0
    )

# Sélection du matériau de la fenêtre
materiaux_fenetre_sud = st.selectbox(
    "Matériaux de fenêtre",
    options=["sélectionner", "Bois", "Metal"],
    index=0
)

st.markdown("### Port - Sud")

# Saisie de la surface totale des portes (en m²)
surface_port_exterieur_sud = st.number_input(
    "Surface totale de porte (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de contact du port
type_contacte_port_sud = st.selectbox(
    "Contact du port",
    options=["type", "Exterieur", "Local Non Chauffé"],
    index=0
)

# Sélection du matériau de la porte
type_port_contacte_sud = st.selectbox(
    "Matériau de porte",
    options=[
        "type",
        "Portes Opaques en Bois",
        "Portes Opaques en Metal",
        "Portes en Bois avec une proportion de vitrage <30%",
        "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
        "Portes en Metal equipées de vitrage simple"
    ],
    index=0
)



#import streamlit as st

st.markdown("## Configuration du mur Est")

# Orientation du mur vers l'Est
var_Est = st.radio(
    "Le mur est-il orienté vers l'Est ?",
    options=["Oui", "Non"],
    index=0
)

if var_Est == "Oui":
    # Affichage de la question sur l'homogénéité du mur Est
    var_homogene_Est = st.radio(
        "Votre mur est-il Homogène ?",
        options=["Oui", "Non"],
        index=0
    )
    
    if var_homogene_Est == "Oui":
        st.markdown("### Configuration pour mur homogène")
        # Affichage d'un champ pour saisir la surface totale du mur Est
        surface_Est = st.number_input("Surface totale du mur Est (m²)", min_value=0.0, value=0.0, step=0.1)
        st.info("Paramètres spécifiques pour un mur homogène seront appliqués.")
    elif var_homogene_Est == "Non":
        st.markdown("### Configuration pour mur non homogène")
        # Affichage des champs pour la configuration non homogène
        surface_fenetre_Est = st.number_input("Surface totale de fenêtre Est (m²)", min_value=0.0, value=0.0, step=0.1)
        surface_Est = st.number_input("Surface totale du mur Est (m²)", min_value=0.0, value=0.0, step=0.1)
        
        type_fenetre_Est = st.selectbox(
            "Type de fenêtre Est",
            options=["Simple", "Double", "Fenetre double"],
            index=0
        )
        
        materiaux_fenetre_Est = st.selectbox(
            "Matériaux de fenêtre Est",
            options=["sélectionner", "Bois", "Metal"],
            index=0
        )
        
        st.markdown("Autres paramètres pour un mur non homogène peuvent être configurés ici.")
else:
    st.write("Configuration du mur Est non requise.")



#import streamlit as st

# --- Données simulées ---
# Exemple de dictionnaire des parois (résistance, masse)
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Est Exemple": (1.5, 200),
        "Mur Est Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

# --- Widgets pour la paroi côté Est ---
st.markdown("## Calcul Déperdition Paroi Est")

selected_mur_Est = st.selectbox(
    "Sélectionnez le mur côté Est",
    options=list(resistance_des_murs.keys())
)

surface_Est = st.number_input(
    "Surface du mur Est (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

def calcul_dep_paroi_Est():
    paroi_choisi_Est = selected_mur_Est
    # surface_Est est déjà un float
    resistance, masse = resistance_des_murs[paroi_choisi_Est]
    coef_k_Est = 1 / resistance if resistance != 0 else 0
    dep_paroi_Est = surface_Est * coef_k_Est
    return dep_paroi_Est

if st.button("Calculer déperdition de la paroi Est"):
    dep_paroi = calcul_dep_paroi_Est()
    st.write(f"Déperdition paroi Est : **{dep_paroi:.3f}**")


# --- Widgets pour la fenêtre côté Est ---
st.markdown("## Calcul Déperdition Fenêtre Est")

type_fenetre_Est = st.selectbox(
    "Type de fenêtre Est",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)

materiaux_fenetre_Est = st.selectbox(
    "Matériaux de fenêtre Est",
    options=["sélectionner", "Bois", "Autre"],
    index=0
)

surface_fenetre_Est = st.number_input(
    "Surface de fenêtre Est (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Pour le cas "Double", demander l'épaisseur (mm)
choix_eppaisseur_Est = None
if type_fenetre_Est == "Double":
    choix_eppaisseur_Est = st.selectbox(
        "Choisissez l'épaisseur (mm) pour fenêtre double",
        options=["5 à 7 ", "8 à 9", "10 à 11", "12 à 13"],
        index=0
    )

def calcul_dep_fenetre_Est():
    choix_fenetre = type_fenetre_Est
    chois_materiaux = materiaux_fenetre_Est
    surface_fenetre = surface_fenetre_Est

    st.write("Type de fenêtre Est :", choix_fenetre)
    if choix_fenetre == "Simple":
        st.write("Vous avez choisi Simple")
        if chois_materiaux == "Bois":
            kwin_Est = 5
        else:
            kwin_Est = 5.8
    elif choix_fenetre == "Double":
        st.write("Vous avez choisi Double")
        if choix_eppaisseur_Est is None:
            st.error("Veuillez sélectionner une épaisseur pour fenêtre double")
            return None
        if chois_materiaux == "Bois":
            if choix_eppaisseur_Est == "5 à 7 ":
                kwin_Est = 3.3
            elif choix_eppaisseur_Est == "8 à 9":
                kwin_Est = 3.1
            elif choix_eppaisseur_Est == "10 à 11":
                kwin_Est = 3
            elif choix_eppaisseur_Est == "12 à 13":
                kwin_Est = 2.9
            else:
                kwin_Est = 5  # valeur par défaut
        else:
            if choix_eppaisseur_Est == "5 à 7 ":
                kwin_Est = 4
            elif choix_eppaisseur_Est == "8 à 9":
                kwin_Est = 3.9
            elif choix_eppaisseur_Est == "10 à 11":
                kwin_Est = 3.8
            elif choix_eppaisseur_Est == "12 à 13":
                kwin_Est = 3.7
            else:
                kwin_Est = 5.8
    elif choix_fenetre == "Fenetre double":
        if chois_materiaux == "Bois":
            kwin_Est = 2.6
        else:
            kwin_Est = 3
    else:
        st.error("Veuillez sélectionner un type de fenêtre valide")
        return None

    st.write("kwin_Est =", kwin_Est)
    r = (1 / kwin_Est) + 0.025 + 0.03 + 0.16
    dep_fenetre_Est = surface_fenetre * (1 / r)
    return dep_fenetre_Est

if st.button("Calculer déperdition de la fenêtre Est"):
    dep_fenetre = calcul_dep_fenetre_Est()
    if dep_fenetre is not None:
        st.write(f"Déperdition fenêtre Est : **{dep_fenetre:.3f}**")


#import streamlit as st

def port_Est():
    # Sélection du type de contact du port
    choix_contact = st.selectbox(
        "Contact du port (Est)",
        options=["Exterieur", "Local Non Chauffé"],
        index=0
    )
    
    # Sélection du type de port
    choix_port = st.selectbox(
        "Type de port",
        options=[
            "Portes Opaques en Bois",
            "Portes Opaques en Metal",
            "Portes en Bois avec une proportion de vitrage <30%",
            "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
            "Portes en Metal equipées de vitrage simple"
        ],
        index=0
    )
    
    # Saisie de la surface du port (en m²)
    surface_port = st.number_input(
        "Surface du port (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    # Calcul de k_port_Est en fonction des choix
    if choix_contact == "Exterieur":
        if choix_port == "Portes Opaques en Bois":
            k_port_Est = 3.5
        elif choix_port == "Portes Opaques en Metal":
            k_port_Est = 5.8
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port_Est = 4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port_Est = 4.5
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port_Est = 5.8
    elif choix_contact == "Local Non Chauffé":
        if choix_port == "Portes Opaques en Bois":
            k_port_Est = 2
        elif choix_port == "Portes Opaques en Metal":
            k_port_Est = 4.5
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port_Est = 2.4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port_Est = 2.7
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port_Est = 4.5
    else:
        k_port_Est = 0  # Valeur par défaut
    
    st.write("k_port_Est =", k_port_Est)
    
    dep_port_Est = surface_port * k_port_Est
    return dep_port_Est

# Bouton pour déclencher le calcul et afficher le résultat
if st.button("Calculer déperdition du port Est"):
    dep = port_Est()
    st.write(f"Déperdition du port Est : {dep:.3f}")


#import streamlit as st

st.markdown("## Calcul de la Déperdition Transmission - Côté Est")

# Widgets pour l'orientation et l'homogénéité du mur Est
var_Est = st.radio("Le mur est-il orienté vers l'Est ?", options=["Oui", "Non"], index=0)
var_homogene_oui_Est = st.radio("Le mur Est est-il homogène ?", options=["Oui", "Non"], index=0)

# Saisie des surfaces (en m²)
surface_Est = st.number_input("Surface du mur Est (m²)", min_value=0.0, value=0.0, step=0.1)
surface_fenetre_Est = st.number_input("Surface des fenêtres Est (m²)", min_value=0.0, value=0.0, step=0.1)
surface_port_Est = st.number_input("Surface des portes Est (m²)", min_value=0.0, value=0.0, step=0.1)

# --- Fonctions de calcul (simulées) ---
def calcul_dep_paroi_Est():
    # Simulation : déperdition paroi = surface_Est * 0.5
    return surface_Est * 0.5

def calcul_dep_fenetre_Est():
    # Simulation : déperdition fenêtre = surface_fenetre_Est * 0.3
    return surface_fenetre_Est * 0.3

def port_Est():
    # Simulation : déperdition port = surface_port_Est * 0.4
    return surface_port_Est * 0.4

# --- Calcul de la déperdition transmission Est ---
def calcul_dep_transmission_Est():
    if var_Est == "Oui":
        dep_paroi = calcul_dep_paroi_Est()
        if var_homogene_oui_Est == "Oui":
            # Pour mur homogène, on considère que la déperdition par les fenêtres et portes est nulle
            dep_fenetre = 0
            dep_port = 0
            surface_fenetre_used = 0
            surface_port_used = 0
            surface_used = surface_Est
        else:
            dep_fenetre = calcul_dep_fenetre_Est()
            dep_port = port_Est()
            surface_used = surface_Est
            surface_fenetre_used = surface_fenetre_Est
            surface_port_used = surface_port_Est
        
        total_surface = surface_used + surface_fenetre_used + surface_port_used
        if total_surface > 0:
            dep_transmission = ((dep_paroi + dep_fenetre + dep_port) / total_surface) * surface_used
        else:
            dep_transmission = 0
        st.write(f"Déperdition transmission Est : **{dep_transmission:.3f}**")
        return dep_transmission
    else:
        st.write("Déperdition transmission Est : **0.000**")
        return 0

# Bouton de calcul
if st.button("Calculer la déperdition transmission côté Est"):
    calcul_dep_transmission_Est()

# --- Mise en page de la section Est ---
st.markdown("---")
st.markdown("### Section Est - Configuration détaillée")
st.info("Ici, vous pouvez ajouter d'autres paramètres et réglages spécifiques au mur Est.")



#import streamlit as st

st.markdown("## Configuration du mur Est")

# Supposons que 'resistance_des_murs' soit un dictionnaire stocké dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Est Exemple 1": (1.5, 200),
        "Mur Est Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur_Est = st.selectbox(
    "Choisissez un mur",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)

# Question : Y a-t-il un mur orienté vers l'Est ?
orientation_Est = st.radio(
    "Y a-t-il un mur orienté vers l'Est ?",
    options=["Oui", "Non"],
    index=0
)

# Question : Votre mur est-il Homogène ?
homogene_Est = st.radio(
    "Votre mur est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)

# Vous pouvez ensuite utiliser les valeurs sélectionnées (selected_mur_Est, orientation_Est, homogene_Est)
st.write("Mur sélectionné :", selected_mur_Est)
st.write("Orientation Est :", orientation_Est)
st.write("Mur homogène :", homogene_Est)




#import streamlit as st

st.markdown("## Configuration du mur Est - Options avancées")

# --- Orientation du mur (via radiobutton) ---
orientation_est = st.radio(
    "Le mur est-il orienté vers l'Est ?",
    options=["Oui", "Non"],
    index=0
)

st.markdown("### Informations sur la fenêtre")

# Saisie de la surface totale de fenêtre (m²) et du mur (m²)
surface_fenetre_est = st.number_input(
    "Surface totale de fenêtre (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
surface_mur_est = st.number_input(
    "Surface totale du mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de fenêtre
type_fenetre_est = st.selectbox(
    "Type de fenêtre",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)

# Si le type "Double" est sélectionné, demander l'épaisseur
epaisseur_est = None
if type_fenetre_est == "Double":
    epaisseur_est = st.selectbox(
        "Épaisseur (mm) pour fenêtre double",
        options=["sélectionner", "5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"],
        index=0
    )

# Sélection du matériau de la fenêtre
materiaux_fenetre_est = st.selectbox(
    "Matériaux de fenêtre",
    options=["sélectionner", "Bois", "Metal"],
    index=0
)

st.markdown("### Informations sur le port")

# Saisie de la surface totale des portes (m²)
surface_port_est = st.number_input(
    "Surface totale de porte (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de contact du port
contact_port_est = st.selectbox(
    "Contact du port",
    options=["type", "Exterieur", "Local Non Chauffé"],
    index=0
)

# Sélection du matériau de la porte
materiau_port_est = st.selectbox(
    "Matériau de porte",
    options=[
        "type",
        "Portes Opaques en Bois",
        "Portes Opaques en Metal",
        "Portes en Bois avec une proportion de vitrage <30%",
        "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
        "Portes en Metal equipées de vitrage simple"
    ],
    index=0
)

# Affichage des valeurs sélectionnées pour vérification
st.markdown("---")
st.markdown("#### Récapitulatif configuration mur Est")
st.write("Orientation du mur Est :", orientation_est)
st.write("Surface fenêtre Est (m²) :", surface_fenetre_est)
st.write("Surface mur Est (m²) :", surface_mur_est)
st.write("Type de fenêtre :", type_fenetre_est)
if epaisseur_est:
    st.write("Épaisseur (mm) :", epaisseur_est)
st.write("Matériaux de fenêtre :", materiaux_fenetre_est)
st.write("Surface port Est (m²) :", surface_port_est)
st.write("Contact port Est :", contact_port_est)
st.write("Matériau de porte :", materiau_port_est)



#import streamlit as st

st.markdown("## Configuration du mur Ouest - Sélection et Homogénéité")

# Simuler les murs déjà créés (par exemple, stockés dans st.session_state)
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Ouest Exemple 1": (1.6, 210),
        "Mur Ouest Exemple 2": (2.1, 260)
    }

# Combobox pour choisir le mur déjà créé
selected_mur_ouest = st.selectbox(
    "Choisissez un mur pour le côté Ouest",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)

# Question : Y a-t-il un mur orienté vers l'Ouest ?
orientation_ouest = st.radio(
    "Le mur est-il orienté vers l'Ouest ?",
    options=["Oui", "Non"],
    index=0
)

# Si le mur est orienté vers l'Ouest, demandez l'homogénéité
if orientation_ouest == "Oui":
    homogene_ouest = st.radio(
        "Votre mur Ouest est-il Homogène ?",
        options=["Oui", "Non"],
        index=0
    )
    st.write("Mur sélectionné :", selected_mur_ouest)
    st.write("Homogénéité :", homogene_ouest)
else:
    st.write("Configuration du mur Ouest ignorée.")



#import streamlit as st

# Exemple de données : dictionnaire des murs (pour le côté Ouest)
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Ouest Exemple 1": (1.5, 200),
        "Mur Ouest Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

# --- Fonction pour calculer la déperdition de la paroi côté Ouest ---
def calcul_dep_paroi_Ouest(surface_Ouest, mur_selection):
    resistance, masse = resistance_des_murs[mur_selection]
    coef_k_Ouest = 1 / resistance if resistance != 0 else 0
    dep_paroi_Ouest = surface_Ouest * coef_k_Ouest
    return dep_paroi_Ouest

# --- Fonction pour calculer la déperdition de la fenêtre côté Ouest ---
def calcul_dep_fenetre_Ouest(type_fenetre, materiau_fenetre, surface_fenetre, epaisseur=None):
    st.write("Type de fenêtre Ouest :", type_fenetre)
    # Détermination de kwin_Ouest selon le type et le matériau
    if type_fenetre == 'Simple':
        if materiau_fenetre == 'Bois':
            kwin_Ouest = 5
        else:
            kwin_Ouest = 5.8
    elif type_fenetre == 'Double':
        if epaisseur is None:
            st.error("Veuillez sélectionner une épaisseur pour fenêtre double.")
            return None
        if materiau_fenetre == 'Bois':
            if epaisseur == "5 à 7":
                kwin_Ouest = 3.3
            elif epaisseur == "8 à 9":
                kwin_Ouest = 3.1
            elif epaisseur == "10 à 11":
                kwin_Ouest = 3
            elif epaisseur == "12 à 13":
                kwin_Ouest = 2.9
            else:
                kwin_Ouest = 5  # valeur par défaut
        else:
            if epaisseur == "5 à 7":
                kwin_Ouest = 4
            elif epaisseur == "8 à 9":
                kwin_Ouest = 3.9
            elif epaisseur == "10 à 11":
                kwin_Ouest = 3.8
            elif epaisseur == "12 à 13":
                kwin_Ouest = 3.7
            else:
                kwin_Ouest = 5.8
    elif type_fenetre == "Fenetre double":
        if materiau_fenetre == 'Bois':
            kwin_Ouest = 2.6
        else:
            kwin_Ouest = 3
    else:
        st.error("Veuillez sélectionner un type de fenêtre valide.")
        return None

    st.write("kwin_Ouest =", kwin_Ouest)
    # Calcul de la résistance totale r et de la déperdition de la fenêtre
    r = (1 / kwin_Ouest) + 0.025 + 0.03 + 0.16
    dep_fenetre_Ouest = surface_fenetre * (1 / r)
    return dep_fenetre_Ouest

# --- Interface de calcul pour le côté Ouest ---

st.markdown("## Calcul Déperdition Côté Ouest")

# Sélection du mur pour la paroi
mur_selection = st.selectbox(
    "Sélectionnez le mur Ouest",
    options=list(resistance_des_murs.keys()),
    index=0
)

# Saisie de la surface du mur (m²)
surface_Ouest = st.number_input("Surface du mur Ouest (m²)", min_value=0.0, value=0.0, step=0.1)

# Bouton de calcul pour la paroi
if st.button("Calculer déperdition paroi Ouest"):
    dep_paroi = calcul_dep_paroi_Ouest(surface_Ouest, mur_selection)
    st.write(f"Déperdition paroi Ouest : **{dep_paroi:.3f}**")

st.markdown("### Déperdition de la fenêtre Ouest")

# Sélection du type de fenêtre
type_fenetre = st.selectbox(
    "Type de fenêtre Ouest",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)

# Sélection du matériau de la fenêtre
materiau_fenetre = st.selectbox(
    "Matériau de fenêtre Ouest",
    options=["sélectionner", "Bois", "Autre"],
    index=0
)

# Saisie de la surface de la fenêtre (m²)
surface_fenetre = st.number_input("Surface de fenêtre Ouest (m²)", min_value=0.0, value=0.0, step=0.1)

# Pour le cas "Double", demande de choisir l'épaisseur
epaisseur = None
if type_fenetre == "Double":
    epaisseur = st.selectbox(
        "Choisissez l'épaisseur (mm) pour fenêtre double",
        options=["5 à 7", "8 à 9", "10 à 11", "12 à 13"],
        index=0
    )

# Bouton de calcul pour la fenêtre
if st.button("Calculer déperdition fenêtre Ouest"):
    dep_fenetre = calcul_dep_fenetre_Ouest(type_fenetre, materiau_fenetre, surface_fenetre, epaisseur)
    if dep_fenetre is not None:
        st.write(f"Déperdition fenêtre Ouest : **{dep_fenetre:.3f}**")


#import streamlit as st

def port_Ouest():
    # Sélection du type de contact du port
    choix_contact = st.selectbox(
        "Contact du port (Ouest)",
        options=["Exterieur", "Local Non Chauffé"],
        index=0
    )
    
    # Sélection du type de porte
    choix_port = st.selectbox(
        "Type de porte (Ouest)",
        options=[
            "Portes Opaques en Bois",
            "Portes Opaques en Metal",
            "Portes en Bois avec une proportion de vitrage <30%",
            "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
            "Portes en Metal equipées de vitrage simple"
        ],
        index=0
    )
    
    # Saisie de la surface du port (en m²)
    surface_port = st.number_input(
        "Surface du port (Ouest) (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    # Calcul de k_port_Ouest selon les choix
    if choix_contact == "Exterieur":
        if choix_port == "Portes Opaques en Bois":
            k_port_Ouest = 3.5
        elif choix_port == "Portes Opaques en Metal":
            k_port_Ouest = 5.8
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port_Ouest = 4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port_Ouest = 4.5
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port_Ouest = 5.8
    elif choix_contact == "Local Non Chauffé":
        if choix_port == "Portes Opaques en Bois":
            k_port_Ouest = 2
        elif choix_port == "Portes Opaques en Metal":
            k_port_Ouest = 4.5
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port_Ouest = 2.4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port_Ouest = 2.7
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port_Ouest = 4.5
    else:
        k_port_Ouest = 0  # Valeur par défaut si besoin

    st.write("k_port_Ouest =", k_port_Ouest)
    dep_port_Ouest = surface_port * k_port_Ouest
    return dep_port_Ouest

if st.button("Calculer déperdition du port Ouest"):
    dep = port_Ouest()
    st.write(f"Déperdition du port Ouest : {dep:.3f}")


#import streamlit as st

st.markdown("## Calcul de la Déperdition Transmission - Côté Ouest")

# --- Saisie des paramètres ---
# Orientation du mur Ouest et homogénéité
var_ouest = st.radio(
    "Le mur est-il orienté vers l'Ouest ?",
    options=["Oui", "Non"],
    index=0
)
var_homogene_ouest = st.radio(
    "Votre mur Ouest est-il homogène ?",
    options=["Oui", "Non"],
    index=0
)

# Saisie des surfaces
surface_ouest = st.number_input("Surface du mur Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
# Si le mur n'est pas homogène, on saisit aussi les surfaces des fenêtres et des portes
if var_homogene_ouest == "Non":
    surface_fenetre_ouest = st.number_input("Surface des fenêtres Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
    surface_port_ouest = st.number_input("Surface des portes Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
else:
    surface_fenetre_ouest = 0
    surface_port_ouest = 0

# --- Fonctions de calcul simulées ---
def calcul_dep_paroi_ouest():
    # Exemple : déperdition paroi = 0.5 * surface du mur
    return surface_ouest * 0.5

def calcul_dep_fenetre_ouest():
    # Exemple : déperdition fenêtre = 0.3 * surface des fenêtres
    return surface_fenetre_ouest * 0.3

def port_ouest():
    # Exemple : déperdition port = 0.4 * surface des portes
    return surface_port_ouest * 0.4

# --- Fonction globale de calcul de la transmission ---
def calcul_dep_transmission_ouest():
    if var_ouest == "Oui":
        dep_paroi = calcul_dep_paroi_ouest()
        if var_homogene_ouest == "Oui":
            dep_fenetre = 0
            dep_port = 0
            s_ouest = surface_ouest
            s_fen = 0
            s_port = 0
        else:
            dep_fenetre = calcul_dep_fenetre_ouest()
            dep_port = port_ouest()
            s_ouest = surface_ouest
            s_fen = surface_fenetre_ouest
            s_port = surface_port_ouest

        total_surface = s_ouest + s_fen + s_port
        if total_surface > 0:
            dep_transmission = ((dep_paroi + dep_fenetre + dep_port) / total_surface) * s_ouest
        else:
            dep_transmission = 0
        st.success(f"Déperdition transmission Ouest : {dep_transmission:.3f}")
        return dep_transmission
    else:
        st.info("Déperdition transmission Ouest : 0.000")
        return 0

# Bouton pour lancer le calcul
if st.button("Calculer déperdition transmission Ouest"):
    calcul_dep_transmission_ouest()

# --- Mise en page supplémentaire pour la section Ouest ---
st.markdown("---")
st.markdown("### Section Ouest - Configuration détaillée")
st.info("Réglages supplémentaires pour le mur Ouest peuvent être configurés ici.")



#import streamlit as st

st.markdown("## Configuration du mur Ouest")

# Supposons que 'resistance_des_murs' soit déjà défini dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Ouest Exemple 1": (1.5, 200),
        "Mur Ouest Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur_ouest = st.selectbox(
    "Mur",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)

# Question : Y a-t-il un mur orienté vers le Ouest ?
orientation_ouest = st.radio(
    "Y a-t-il un mur orienté vers le Ouest ?",
    options=["Oui", "Non"],
    index=0
)

# Question : Votre mur Ouest est-il Homogène ?
homogene_ouest = st.radio(
    "Votre mur Ouest est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)

st.write("Mur sélectionné :", selected_mur_ouest)
st.write("Orientation :", orientation_ouest)
st.write("Homogénéité :", homogene_ouest)

# Optionnel : Bouton pour valider et appeler une fonction (par exemple, paroi_Ouest_homgene)
if st.button("Valider configuration Ouest"):
    # Par exemple, appelez ici votre fonction paroi_Ouest_homgene adaptée à Streamlit
    st.success("Configuration validée.")



#import streamlit as st

st.markdown("## Configuration du mur Ouest - Options avancées")

# Radiobutton pour l'orientation vers Ouest
orientation_ouest = st.radio(
    "Le mur est-il orienté vers l'Ouest ?",
    options=["Oui", "Non"],
    index=0
)

# Section pour la configuration des surfaces et options de la fenêtre côté Ouest
st.markdown("### Configuration de la fenêtre côté Ouest")

# Saisie de la surface totale de fenêtre (m²)
surface_fenetre_ouest = st.number_input(
    "Surface totale de fenêtre (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Saisie de la surface totale du mur (m²)
surface_mur_ouest = st.number_input(
    "Surface totale du mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de fenêtre
type_fenetre_ouest = st.selectbox(
    "Type de fenêtre",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)

# Sélection du matériau de la fenêtre
materiaux_fenetre_ouest = st.selectbox(
    "Matériaux de fenêtre",
    options=["sélectionner", "Bois", "Metal"],
    index=0
)

# Pour le cas "Double", demander l'épaisseur (mm)
epaisseur_ouest = None
if type_fenetre_ouest == "Double":
    epaisseur_ouest = st.selectbox(
        "Épaisseur (mm) pour fenêtre double",
        options=["sélectionner", "5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"],
        index=0
    )

# Section pour la configuration du port côté Ouest
st.markdown("### Configuration du port côté Ouest")

# Saisie de la surface totale des portes (m²)
surface_port_ouest = st.number_input(
    "Surface totale de porte (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Sélection du type de contact du port
contact_port_ouest = st.selectbox(
    "Contact du port",
    options=["type", "Exterieur", "Local Non Chauffé"],
    index=0
)

# Sélection du matériau de la porte
materiau_port_ouest = st.selectbox(
    "Matériau de porte",
    options=[
        "type",
        "Portes Opaques en Bois",
        "Portes Opaques en Metal",
        "Portes en Bois avec une proportion de vitrage <30%",
        "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
        "Portes en Metal equipées de vitrage simple"
    ],
    index=0
)

# Récapitulatif de la configuration côté Ouest
st.markdown("### Récapitulatif configuration côté Ouest")
st.write("Orientation du mur :", orientation_ouest)
st.write("Surface du mur (m²) :", surface_mur_ouest)
st.write("Surface de fenêtre (m²) :", surface_fenetre_ouest)
st.write("Type de fenêtre :", type_fenetre_ouest)
if epaisseur_ouest:
    st.write("Épaisseur (mm) :", epaisseur_ouest)
st.write("Matériaux de fenêtre :", materiaux_fenetre_ouest)
st.write("Surface de porte (m²) :", surface_port_ouest)
st.write("Contact du port :", contact_port_ouest)
st.write("Matériau de porte :", materiau_port_ouest)



#import streamlit as st

st.markdown("## Configuration du mur Nord-Est")

# Demander si le mur Nord-Est est orienté
var_Nord_Est = st.radio(
    "Le mur Nord-Est est-il orienté ?",
    options=["Oui", "Non"],
    index=0
)

if var_Nord_Est == "Oui":
    st.markdown("### Homogénéité du mur Nord-Est")
    var_homogene_oui_Nord_Est = st.radio(
        "Votre mur Nord-Est est-il homogène ?",
        options=["Oui", "Non"],
        index=0
    )
    
    if var_homogene_oui_Nord_Est == "Oui":
        st.markdown("#### Configuration pour mur homogène")
        # Afficher le champ pour la surface totale du mur
        surface_Nord_Est = st.number_input("Surface totale du mur Nord-Est (m²)", min_value=0.0, value=0.0, step=0.1)
        st.write("Surface du mur Nord-Est :", surface_Nord_Est, "m²")
        st.info("Configuration homogène activée.")
    elif var_homogene_oui_Nord_Est == "Non":
        st.markdown("#### Configuration pour mur non homogène")
        # Afficher les champs pour saisir les surfaces de fenêtre et de mur
        surface_fenetre_Nord_Est = st.number_input("Surface totale de fenêtre Nord-Est (m²)", min_value=0.0, value=0.0, step=0.1)
        surface_Nord_Est = st.number_input("Surface totale du mur Nord-Est (m²)", min_value=0.0, value=0.0, step=0.1)
        # Afficher les options pour le type de fenêtre et le matériau
        type_fenetre_Nord_Est = st.selectbox("Type de fenêtre Nord-Est", options=["Simple", "Double", "Fenetre double"])
        materiaux_fenetre_Nord_Est = st.selectbox("Matériaux de fenêtre Nord-Est", options=["Bois", "Metal"])
        st.markdown("Configuration non homogène activée.")
else:
    st.write("Aucun mur Nord-Est configuré.")



#import streamlit as st

# On s'assure que le dictionnaire des murs est défini dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Nord-Est Exemple 1": (1.5, 200),
        "Mur Nord-Est Exemple 2": (2.0, 250)
    }

def calcul_dep_paroi_Nord_Est(selected_mur, surface):
    resistance, poid = st.session_state.resistance_des_murs[selected_mur]
    coef = 1 / resistance if resistance != 0 else 0
    dep_paroi = surface * coef
    masse_paroi = surface * poid  # Calcul de la masse (non utilisé ici)
    return dep_paroi

st.markdown("## Calcul de la Déperdition de la Paroi Nord-Est")

# Sélection du mur déjà créé
selected_mur = st.selectbox(
    "Sélectionnez le mur Nord-Est",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)

# Saisie de la surface du mur en m²
surface = st.number_input(
    "Surface du mur Nord-Est (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Bouton pour lancer le calcul
if st.button("Calculer déperdition paroi Nord-Est"):
    dep = calcul_dep_paroi_Nord_Est(selected_mur, surface)
    st.write(f"Déperdition paroi Nord-Est : **{dep:.3f}**")



#import streamlit as st

def calcul_dep_fenetre_Nord_Est():
    # Sélection du type de fenêtre
    choix_fenetre = st.selectbox(
        "Type de fenêtre Nord-Est",
        options=["Simple", "Double", "Fenetre double"],
        index=0
    )
    
    # Sélection du matériau de la fenêtre
    choix_materiaux = st.selectbox(
        "Matériaux de fenêtre Nord-Est",
        options=["Bois", "Metal"],
        index=0
    )
    
    # Saisie de la surface de la fenêtre (en m²)
    surface_fenetre = st.number_input(
        "Surface de la fenêtre Nord-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    st.write("Type de fenêtre choisi :", choix_fenetre)
    
    # Calcul du coefficient kwin en fonction des choix
    if choix_fenetre == 'Simple':
        st.write("Vous avez choisi une fenêtre simple.")
        if choix_materiaux == 'Bois':
            kwin = 5
        else:
            kwin = 5.8
    elif choix_fenetre == 'Double':
        st.write("Vous avez choisi une fenêtre double.")
        # Demander la sélection de l'épaisseur
        choix_epaisseur = st.selectbox(
            "Choisissez l'épaisseur (mm) pour fenêtre double",
            options=["5 à 7", "8 à 9", "10 à 11", "12 à 13"],
            index=0
        )
        if choix_materiaux == 'Bois':
            if choix_epaisseur == "5 à 7":
                kwin = 3.3
            elif choix_epaisseur == "8 à 9":
                kwin = 3.1
            elif choix_epaisseur == "10 à 11":
                kwin = 3.0
            elif choix_epaisseur == "12 à 13":
                kwin = 2.9
            else:
                kwin = 5  # valeur par défaut
        else:
            if choix_epaisseur == "5 à 7":
                kwin = 4.0
            elif choix_epaisseur == "8 à 9":
                kwin = 3.9
            elif choix_epaisseur == "10 à 11":
                kwin = 3.8
            elif choix_epaisseur == "12 à 13":
                kwin = 3.7
            else:
                kwin = 5.8  # valeur par défaut
    elif choix_fenetre == "Fenetre double":
        if choix_materiaux == 'Bois':
            kwin = 2.6
        else:
            kwin = 3.0
    else:
        st.error("Veuillez sélectionner un type de fenêtre valide.")
        return None

    st.write("kwin =", kwin)
    
    # Calcul de la résistance totale et de la déperdition
    r = (1 / kwin) + 0.025 + 0.03 + 0.16
    dep_fenetre = surface_fenetre * (1 / r)
    
    return dep_fenetre

# Bouton pour lancer le calcul et afficher le résultat
if st.button("Calculer déperdition fenêtre Nord-Est"):
    dep = calcul_dep_fenetre_Nord_Est()
    if dep is not None:
        st.write(f"Déperdition fenêtre Nord-Est : {dep:.3f}")



#import streamlit as st

def port_Nord_Est():
    # Sélection du type de contact du port
    contact_option = st.selectbox(
        "Contact du port (Nord-Est)",
        options=["Exterieur", "Local Non Chauffé"],
        index=0
    )
    
    # Sélection du type de porte
    porte_option = st.selectbox(
        "Type de porte (Nord-Est)",
        options=[
            "Portes Opaques en Bois",
            "Portes Opaques en Metal",
            "Portes en Bois avec une proportion de vitrage <30%",
            "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
            "Portes en Metal equipées de vitrage simple"
        ],
        index=0
    )
    
    # Saisie de la surface du port (en m²)
    surface_port = st.number_input(
        "Surface du port (Nord-Est) (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    # Calcul du coefficient k_port_Nord_Est selon les choix
    if contact_option == "Exterieur":
        if porte_option == "Portes Opaques en Bois":
            k_port = 3.5
        elif porte_option == "Portes Opaques en Metal":
            k_port = 5.8
        elif porte_option == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 4
        elif porte_option == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 4.5
        elif porte_option == "Portes en Metal equipées de vitrage simple":
            k_port = 5.8
    elif contact_option == "Local Non Chauffé":
        if porte_option == "Portes Opaques en Bois":
            k_port = 2
        elif porte_option == "Portes Opaques en Metal":
            k_port = 4.5
        elif porte_option == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 2.4
        elif porte_option == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 2.7
        elif porte_option == "Portes en Metal equipées de vitrage simple":
            k_port = 4.5
    else:
        k_port = 0

    st.write("k_port_Nord_Est =", k_port)
    
    dep_port = surface_port * k_port
    return dep_port

if st.button("Calculer déperdition du port Nord-Est"):
    dep = port_Nord_Est()
    st.write(f"Déperdition du port Nord-Est : {dep:.3f}")
    

#import streamlit as st

st.markdown("## Calcul de la Déperdition Transmission - Côté Nord-Est")

# Choix de présence du mur Nord-Est
var_Nord_Est = st.radio(
    "Le mur Nord-Est est-il présent ?",
    options=["Oui", "Non"],
    index=0
)

if var_Nord_Est == "Oui":
    # Choix de l'homogénéité du mur
    var_homogene_oui_Nord_Est = st.radio(
        "Le mur Nord-Est est-il homogène ?",
        options=["Oui", "Non"],
        index=0
    )
    
    if var_homogene_oui_Nord_Est == "Oui":
        # Pour un mur homogène, on considère que la déperdition par les fenêtres et portes est nulle.
        surface_Nord_Est = st.number_input("Surface du mur Nord-Est (m²)", min_value=0.0, value=0.0, step=0.1)
        surface_fenetre_Nord_Est = 0.0
        surface_port_Nord_Est = 0.0
        dep_fenetre_Nord_Est = 0.0
        dep_port_Nord_Est = 0.0
    else:
        # Pour un mur non homogène, saisir toutes les surfaces et déperditions
        surface_Nord_Est = st.number_input("Surface du mur Nord-Est (m²)", min_value=0.0, value=0.0, step=0.1)
        surface_fenetre_Nord_Est = st.number_input("Surface des fenêtres Nord-Est (m²)", min_value=0.0, value=0.0, step=0.1)
        surface_port_Nord_Est = st.number_input("Surface des portes Nord-Est (m²)", min_value=0.0, value=0.0, step=0.1)
        dep_fenetre_Nord_Est = st.number_input("Déperdition des fenêtres Nord-Est (W)", min_value=0.0, value=0.0, step=0.1)
        dep_port_Nord_Est = st.number_input("Déperdition des portes Nord-Est (W)", min_value=0.0, value=0.0, step=0.1)
    
    # Saisie de la déperdition de la paroi Nord-Est (en W)
    dep_paroi_Nord_Est = st.number_input("Déperdition de la paroi Nord-Est (W)", min_value=0.0, value=0.0, step=0.1)
    
    total_surface = surface_Nord_Est + surface_fenetre_Nord_Est + surface_port_Nord_Est
    if total_surface > 0:
        dep_transmission_Nord_Est = ((dep_paroi_Nord_Est + dep_fenetre_Nord_Est + dep_port_Nord_Est) / total_surface) * surface_Nord_Est
    else:
        dep_transmission_Nord_Est = 0
    st.success(f"Déperdition transmission Nord-Est : {dep_transmission_Nord_Est:.3f} W")
else:
    st.info("Déperdition transmission Nord-Est : 0.000 W")


#import streamlit as st

st.markdown("## Configuration du mur Nord-Est")

# Supposons que le dictionnaire des parois soit stocké dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Nord-Est Exemple 1": (1.5, 200),
        "Mur Nord-Est Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur_nord_est = st.selectbox(
    "Mur",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)
st.write("Mur sélectionné :", selected_mur_nord_est)

# Question : Y a-t-il un mur orienté vers le Nord-Est ?
orientation_nord_est = st.radio(
    "Y a-t-il un mur orienté vers le Nord-Est ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Orientation :", orientation_nord_est)

# Question : Votre mur Nord-Est est-il Homogène ?
homogene_nord_est = st.radio(
    "Votre mur Nord-Est est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Homogénéité :", homogene_nord_est)

# Optionnel : Exécution d'une fonction de configuration en fonction de la réponse
if homogene_nord_est == "Oui":
    st.info("Configuration pour mur homogène activée.")
else:
    st.info("Configuration pour mur non homogène activée.")



#import streamlit as st

st.markdown("## Configuration du mur Nord-Est - Options avancées")

# --- Orientation du mur Nord-Est ---
orientation_nord_est = st.radio(
    "Le mur Nord-Est est-il orienté ?",
    options=["Oui", "Non"],
    index=0
)

# --- Combobox pour choisir le mur déjà créé ---
# (Supposons que le dictionnaire des murs est stocké dans st.session_state)
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Nord-Est Exemple 1": (1.5, 200),
        "Mur Nord-Est Exemple 2": (2.0, 250)
    }
selected_mur_nord_est = st.selectbox(
    "Mur",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)

# --- Questions sur l'orientation et l'homogénéité ---
orientation_question = st.radio(
    "Y a-t-il un mur orienté vers le Nord-Est ?",
    options=["Oui", "Non"],
    index=0
)
homogene_question = st.radio(
    "Votre mur Nord-Est est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)

# --- Configuration de la fenêtre côté Nord-Est ---
st.markdown("### Configuration de la fenêtre Nord-Est")
surface_fenetre_nord_est = st.number_input(
    "Surface totale de fenêtre (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
surface_mur_nord_est = st.number_input(
    "Surface totale du mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
type_fenetre_nord_est = st.selectbox(
    "Type de fenêtre",
    options=["sélectionner", "Simple", "Double", "Fenetre double"],
    index=0
)
materiaux_fenetre_nord_est = st.selectbox(
    "Matériaux de fenêtre",
    options=["sélectionner", "Bois", "Metal"],
    index=0
)
epaisseur_aim_dair_nord_est = None
if type_fenetre_nord_est == "Double":
    epaisseur_aim_dair_nord_est = st.selectbox(
        "Épaisseur (mm) pour fenêtre double",
        options=["sélectionner", "5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"],
        index=0
    )

# --- Configuration du port côté Nord-Est ---
st.markdown("### Configuration du port Nord-Est")
surface_port_nord_est = st.number_input(
    "Surface totale de porte (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
contact_port_nord_est = st.selectbox(
    "Contact avec",
    options=["type", "Exterieur", "Local Non Chauffé"],
    index=0
)
type_port_nord_est = st.selectbox(
    "Matériau de Porte",
    options=[
        "type",
        "Portes Opaques en Bois",
        "Portes Opaques en Metal",
        "Portes en Bois avec une proportion de vitrage <30%",
        "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
        "Portes en Metal equipées de vitrage simple"
    ],
    index=0
)

# --- Récapitulatif de la configuration ---
st.markdown("### Récapitulatif configuration Nord-Est")
st.write("Mur sélectionné :", selected_mur_nord_est)
st.write("Orientation du mur :", orientation_nord_est)
st.write("Question orientation Nord-Est :", orientation_question)
st.write("Homogénéité :", homogene_question)
st.write("Surface fenêtre (m²) :", surface_fenetre_nord_est)
st.write("Surface mur (m²) :", surface_mur_nord_est)
st.write("Type de fenêtre :", type_fenetre_nord_est)
st.write("Matériaux de fenêtre :", materiaux_fenetre_nord_est)
if epaisseur_aim_dair_nord_est:
    st.write("Épaisseur (mm) :", epaisseur_aim_dair_nord_est)
st.write("Surface porte (m²) :", surface_port_nord_est)
st.write("Contact port :", contact_port_nord_est)
st.write("Matériau de porte :", type_port_nord_est)


#import streamlit as st

st.markdown("## Configuration du mur Nord-Ouest")

# Demander si le mur Nord-Ouest est présent
var_Nord_Ouest = st.radio(
    "Le mur Nord-Ouest est-il présent ?",
    options=["Oui", "Non"],
    index=0
)

if var_Nord_Ouest == "Oui":
    st.markdown("### Votre mur Nord-Ouest est Homogène ?")
    # Choix de l'homogénéité
    homogene_nord_ouest = st.radio(
        "Votre mur Nord-Ouest est-il Homogène ?",
        options=["Oui", "Non"],
        index=0
    )
    st.write("Options de configuration pour mur homogène activées.")
    # Ici, vous pouvez ajouter d'autres widgets pour configurer les paramètres si besoin.
else:
    st.write("La configuration du mur Nord-Ouest est masquée.")



#import streamlit as st

st.markdown("## Configuration du mur Nord-Est")

# Dictionnaire simulé pour les parois (stocké dans st.session_state)
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Nord-Est Exemple": (1.5, 200),
        "Mur Nord-Est Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

# Combobox pour choisir le mur déjà créé
selected_mur = st.selectbox(
    "Choisissez le mur Nord-Est",
    options=list(resistance_des_murs.keys()),
    index=0
)

# Radiobutton pour l'orientation vers Nord-Est (simulé via st.radio)
var_Nord_Est = st.radio(
    "Le mur Nord-Est est-il orienté ?",
    options=["Oui", "Non"],
    index=0
)

# Questions sur l'homogénéité du mur Nord-Est
st.markdown("### Configuration Homogénéité")
var_homogene_oui_Nord_Est = st.radio(
    "Votre mur Nord-Est est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)

# En fonction de la réponse sur l'homogénéité, afficher des champs différents
if var_homogene_oui_Nord_Est == "Oui":
    st.info("Configuration pour mur homogène activée.")
    # Pour un mur homogène, on demande uniquement la surface du mur
    surface_Nord_Est = st.number_input(
        "Surface totale du mur Nord-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    # Les champs pour les fenêtres et autres options ne sont pas affichés
else:
    st.info("Configuration pour mur non homogène activée.")
    # Pour un mur non homogène, on demande la surface des fenêtres et celle du mur
    surface_fenetre_Nord_Est = st.number_input(
        "Surface totale de fenêtre Nord-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    surface_Nord_Est = st.number_input(
        "Surface totale du mur Nord-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    # On affiche aussi des options supplémentaires pour la configuration de la fenêtre
    type_fenetre_Nord_Est = st.selectbox(
        "Type de fenêtre Nord-Est",
        options=["Simple", "Double", "Fenetre double"],
        index=0
    )
    materiaux_fenetre_Nord_Est = st.selectbox(
        "Matériaux de fenêtre Nord-Est",
        options=["Bois", "Metal"],
        index=0
    )
    # Vous pouvez ajouter ici d'autres options (par exemple, l'épaisseur pour une fenêtre double)

# Fonction pour calculer la déperdition de la paroi Nord-Est
def calcul_dep_paroi_Nord_Est(selected_mur, surface):
    resistance, poid = resistance_des_murs[selected_mur]
    coef_k = 1 / resistance if resistance != 0 else 0
    dep_paroi = surface * coef_k
    # Masse de la paroi (calculée mais non utilisée ici)
    masse_paroi = surface * poid
    return dep_paroi

# Bouton pour lancer le calcul et afficher le résultat
if st.button("Calculer déperdition paroi Nord-Est"):
    dep = calcul_dep_paroi_Nord_Est(selected_mur, surface_Nord_Est)
    st.success(f"Déperdition paroi Nord-Est : {dep:.3f}")



#import streamlit as st

def calcul_dep_fenetre_Nord_Ouest():
    # Sélection du type de fenêtre
    choix_fenetre = st.selectbox(
        "Type de fenêtre Nord-Ouest",
        options=["Simple", "Double", "Fenetre double"],
        index=0
    )
    
    # Sélection du matériau de la fenêtre
    materiau = st.selectbox(
        "Matériaux de fenêtre Nord-Ouest",
        options=["Bois", "Metal"],
        index=0
    )
    
    # Saisie de la surface de la fenêtre (en m²)
    surface = st.number_input(
        "Surface de fenêtre Nord-Ouest (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    st.write("Type de fenêtre choisi :", choix_fenetre)
    
    # Détermination de kwin en fonction des choix
    if choix_fenetre == 'Simple':
        st.write("Vous avez choisi une fenêtre simple.")
        if materiau == 'Bois':
            kwin = 5
        else:
            kwin = 5.8
    elif choix_fenetre == 'Double':
        st.write("Vous avez choisi une fenêtre double.")
        # Demander la sélection de l'épaisseur
        epaisseur = st.selectbox(
            "Choisissez l'épaisseur (mm) pour fenêtre double",
            options=["5 à 7", "8 à 9", "10 à 11", "12 à 13"],
            index=0
        )
        if materiau == 'Bois':
            if epaisseur == "5 à 7":
                kwin = 3.3
            elif epaisseur == "8 à 9":
                kwin = 3.1
            elif epaisseur == "10 à 11":
                kwin = 3.0
            elif epaisseur == "12 à 13":
                kwin = 2.9
            else:
                kwin = 5  # valeur par défaut
        else:
            if epaisseur == "5 à 7":
                kwin = 4
            elif epaisseur == "8 à 9":
                kwin = 3.9
            elif epaisseur == "10 à 11":
                kwin = 3.8
            elif epaisseur == "12 à 13":
                kwin = 3.7
            else:
                kwin = 5.8
    elif choix_fenetre == "Fenetre double":
        if materiau == 'Bois':
            kwin = 2.6
        else:
            kwin = 3
    else:
        st.error("Veuillez sélectionner un type de fenêtre valide.")
        return None

    st.write("kwin =", kwin)
    
    # Calcul de la résistance totale r et de la déperdition de la fenêtre
    r = (1 / kwin) + 0.025 + 0.03 + 0.16
    dep_fenetre = surface * (1 / r)
    return dep_fenetre

if st.button("Calculer déperdition fenêtre Nord-Ouest"):
    dep_value = calcul_dep_fenetre_Nord_Ouest()
    if dep_value is not None:
        st.write(f"Déperdition de la fenêtre Nord-Ouest : {dep_value:.3f}")


#import streamlit as st

def port_Nord_Ouest():
    # Sélection du type de contact du port
    choix_contact = st.selectbox(
        "Contact du port (Nord-Ouest)",
        options=["Exterieur", "Local Non Chauffé"],
        index=0
    )
    
    # Sélection du type de porte
    choix_port = st.selectbox(
        "Type de porte (Nord-Ouest)",
        options=[
            "Portes Opaques en Bois",
            "Portes Opaques en Metal",
            "Portes en Bois avec une proportion de vitrage <30%",
            "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
            "Portes en Metal equipées de vitrage simple"
        ],
        index=0
    )
    
    # Saisie de la surface du port (en m²)
    surface_port = st.number_input(
        "Surface du port (Nord-Ouest) (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    # Calcul de k_port_Nord_Ouest selon les choix
    if choix_contact == "Exterieur":
        if choix_port == "Portes Opaques en Bois":
            k_port = 3.5
        elif choix_port == "Portes Opaques en Metal":
            k_port = 5.8
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 4.0
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 4.5
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port = 5.8
    elif choix_contact == "Local Non Chauffé":
        if choix_port == "Portes Opaques en Bois":
            k_port = 2.0
        elif choix_port == "Portes Opaques en Metal":
            k_port = 4.5
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 2.4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 2.7
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port = 4.5
    else:
        k_port = 0

    st.write("k_port_Nord_Ouest =", k_port)
    
    dep_port = surface_port * k_port
    return dep_port

if st.button("Calculer déperdition du port Nord-Ouest"):
    dep_value = port_Nord_Ouest()
    st.write(f"Déperdition du port Nord-Ouest : {dep_value:.3f}")


#import streamlit as st

st.markdown("## Calcul de la Déperdition Transmission - Côté Nord-Ouest")

# On demande si le mur Nord-Ouest est présent
var_Nord_Ouest = st.radio(
    "Le mur Nord-Ouest est-il présent ?",
    options=["Oui", "Non"],
    index=0
)

if var_Nord_Ouest == "Oui":
    st.subheader("Configuration du mur Nord-Ouest")
    # Demande si le mur est homogène
    var_homogene_oui_Nord_Ouest = st.radio(
        "Votre mur Nord-Ouest est-il homogène ?",
        options=["Oui", "Non"],
        index=0
    )
    
    if var_homogene_oui_Nord_Ouest == "Oui":
        # Pour un mur homogène, seules la surface du mur et la déperdition de la paroi sont saisies.
        surface_Nord_Ouest = st.number_input("Surface du mur Nord-Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
        # Pour un mur homogène, on suppose que la déperdition par les fenêtres et portes est nulle.
        surface_fenetre_Nord_Ouest = 0.0
        surface_port_Nord_Ouest = 0.0
        dep_fenetre_Nord_Ouest = 0.0
        dep_port_Nord_Ouest = 0.0
    else:
        # Pour un mur non homogène, on demande les surfaces et déperditions pour fenêtres et portes.
        surface_Nord_Ouest = st.number_input("Surface du mur Nord-Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
        surface_fenetre_Nord_Ouest = st.number_input("Surface des fenêtres Nord-Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
        surface_port_Nord_Ouest = st.number_input("Surface des portes Nord-Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
        dep_fenetre_Nord_Ouest = st.number_input("Déperdition des fenêtres Nord-Ouest (W)", min_value=0.0, value=0.0, step=0.1)
        dep_port_Nord_Ouest = st.number_input("Déperdition des portes Nord-Ouest (W)", min_value=0.0, value=0.0, step=0.1)
    
    # Saisie de la déperdition de la paroi Nord-Ouest (en W)
    dep_paroi_Nord_Ouest = st.number_input("Déperdition de la paroi Nord-Ouest (W)", min_value=0.0, value=0.0, step=0.1)
    
    # Calcul de la déperdition de transmission
    total_surface = surface_Nord_Ouest + surface_fenetre_Nord_Ouest + surface_port_Nord_Ouest
    if total_surface > 0:
        dep_transmission_Nord_Ouest = ((dep_paroi_Nord_Ouest + dep_fenetre_Nord_Ouest + dep_port_Nord_Ouest) / total_surface) * surface_Nord_Ouest
    else:
        dep_transmission_Nord_Ouest = 0.0

    st.success(f"Déperdition transmission Nord-Ouest : {dep_transmission_Nord_Ouest:.3f} W")
else:
    st.info("Déperdition transmission Nord-Ouest : 0.000 W")

st.markdown("---")
st.markdown("### Section Nord-Ouest - Configuration détaillée")



#import streamlit as st

st.markdown("## Configuration du mur Nord-Ouest")

# On suppose que le dictionnaire des murs existe dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Nord-Ouest Exemple 1": (1.5, 200),
        "Mur Nord-Ouest Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur = st.selectbox(
    "Mur",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)
st.write("Mur sélectionné :", selected_mur)

# Question : Y a-t-il un mur orienté vers le Nord-Ouest ?
orientation_nord_ouest = st.radio(
    "Y a-t-il un mur orienté vers le Nord-Ouest ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Orientation Nord-Ouest :", orientation_nord_ouest)

# Question : Votre mur Nord-Ouest est-il Homogène ?
homogene_nord_ouest = st.radio(
    "Votre mur Nord-Ouest est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Homogénéité :", homogene_nord_ouest)

# Vous pouvez appeler ici une fonction de configuration en fonction de la réponse
if homogene_nord_ouest == "Oui":
    st.info("Configuration pour mur homogène activée.")
else:
    st.info("Configuration pour mur non homogène activée.")


#import streamlit as st

st.markdown("## Configuration du mur Nord-Ouest - Options avancées")

# --- Choix du mur déjà créé ---
# On suppose que le dictionnaire des parois est stocké dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Nord-Ouest Exemple 1": (1.5, 200),
        "Mur Nord-Ouest Exemple 2": (2.0, 250)
    }
selected_mur = st.selectbox(
    "Mur",
    options=list(st.session_state.resistance_des_murs.keys()),
    index=0
)
st.write("Mur sélectionné :", selected_mur)

# --- Orientation et homogénéité ---
orientation_nord_ouest = st.radio(
    "Y a-t-il un mur orienté vers le Nord-Ouest ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Orientation :", orientation_nord_ouest)

homogene_nord_ouest = st.radio(
    "Votre mur Nord-Ouest est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Homogénéité :", homogene_nord_ouest)

# --- Configuration de la fenêtre ---
st.markdown("### Configuration de la fenêtre Nord-Ouest")
surface_fenetre = st.number_input(
    "Surface totale de fenêtre (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
surface_mur = st.number_input(
    "Surface totale du mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
type_fenetre_options = ["Simple", "Double", "Fenetre double"]
type_fenetre = st.selectbox(
    "Type de fenêtre",
    options=type_fenetre_options,
    index=0
)
materiaux_options = ["Bois", "Metal"]
materiaux_fenetre = st.selectbox(
    "Matériaux de fenêtre",
    options=materiaux_options,
    index=0
)
epaisseur_options = ["5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"]
epaisseur = None
if type_fenetre == "Double":
    epaisseur = st.selectbox(
        "Épaisseur (mm) pour fenêtre double",
        options=epaisseur_options,
        index=0
    )

# --- Configuration du port ---
st.markdown("### Configuration du port Nord-Ouest")
surface_port = st.number_input(
    "Surface totale de porte (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
contact_options = ["Exterieur", "Local Non Chauffé"]
contact_port = st.selectbox(
    "Contact avec",
    options=contact_options,
    index=0
)
materiaux_port_options = [
    "Portes Opaques en Bois",
    "Portes Opaques en Metal",
    "Portes en Bois avec une proportion de vitrage <30%",
    "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
    "Portes en Metal equipées de vitrage simple"
]
materiau_port = st.selectbox(
    "Matériau de Porte",
    options=materiaux_port_options,
    index=0
)

# Récapitulatif de la configuration
st.markdown("### Récapitulatif configuration Nord-Ouest")
st.write("Mur sélectionné :", selected_mur)
st.write("Orientation Nord-Ouest :", orientation_nord_ouest)
st.write("Homogénéité :", homogene_nord_ouest)
st.write("Surface fenêtre (m²) :", surface_fenetre)
st.write("Surface mur (m²) :", surface_mur)
st.write("Type de fenêtre :", type_fenetre)
st.write("Matériaux de fenêtre :", materiaux_fenetre)
if epaisseur:
    st.write("Épaisseur (mm) :", epaisseur)
st.write("Surface porte (m²) :", surface_port)
st.write("Contact du port :", contact_port)
st.write("Matériau de porte :", materiau_port)


import streamlit as st

st.markdown("## Configuration du mur Sud-Est")

def paroi_Sud_Est():
    # Demande si le mur Sud-Est est présent
    presence = st.radio(
        "Le mur Sud-Est est-il présent ?",
        options=["Oui", "Non"],
        index=0,
        key="presence_sud_est"
    )
    
    if presence == "Oui":
        st.markdown("### Votre mur Sud-Est est Homogène ?")
        homogene = st.radio(
            "Votre mur Sud-Est est-il Homogène ?",
            options=["Oui", "Non"],
            index=0,
            key="homogene_sud_est"
        )
        st.write("Options pour mur homogène affichées.")
    else:
        st.write("La configuration du mur Sud-Est est masquée.")

# Appel de la fonction pour afficher l'interface
paroi_Sud_Est()


#import streamlit as st

st.markdown("## Configuration du mur Sud-Est - Homogénéité")

# Choix de l'homogénéité du mur Sud-Est
homogene_sud_est = st.radio(
    "Votre mur Sud-Est est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)

if homogene_sud_est == "Oui":
    st.info("Configuration pour mur homogène activée.")
    # Pour un mur homogène, on affiche uniquement la saisie de la surface du mur
    surface_sud_est = st.number_input("Surface totale du mur Sud-Est (m²)", min_value=0.0, value=0.0, step=0.1)
    st.write("Surface du mur Sud-Est :", surface_sud_est, "m²")
else:
    st.info("Configuration pour mur non homogène activée.")
    # Pour un mur non homogène, on affiche la saisie de la surface des fenêtres et du mur
    surface_fenetre_sud_est = st.number_input("Surface totale de fenêtre Sud-Est (m²)", min_value=0.0, value=0.0, step=0.1)
    surface_sud_est = st.number_input("Surface totale du mur Sud-Est (m²)", min_value=0.0, value=0.0, step=0.1)
    # Sélection du type de fenêtre et du matériau
    type_fenetre_sud_est = st.selectbox("Type de fenêtre Sud-Est", options=["Simple", "Double", "Fenetre double"], index=0)
    materiaux_fenetre_sud_est = st.selectbox("Matériaux de fenêtre Sud-Est", options=["Bois", "Metal"], index=0)
    st.markdown("Options supplémentaires pour mur non homogène activées.")

#import streamlit as st

# On s'assure que le dictionnaire des murs est défini
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Sud-Est Exemple": (1.5, 200),
        "Mur Sud-Est Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

def calcul_dep_paroi_Sud_Est(selected_mur, surface):
    # Récupération des paramètres du mur sélectionné
    resistance, poid = resistance_des_murs[selected_mur]
    coef_k = 1 / resistance if resistance != 0 else 0
    dep_paroi = surface * coef_k
    # Masse de la paroi calculée (non utilisée ici)
    masse_paroi = surface * poid
    return dep_paroi

st.markdown("## Calcul de la Déperdition de la Paroi - Côté Sud-Est")

# Sélection du mur (combobox)
selected_mur = st.selectbox(
    "Sélectionnez le mur Sud-Est",
    options=list(resistance_des_murs.keys())
)

# Saisie de la surface du mur (entry)
surface_val = st.number_input(
    "Surface du mur Sud-Est (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Bouton pour lancer le calcul
if st.button("Calculer déperdition paroi Sud-Est"):
    dep = calcul_dep_paroi_Sud_Est(selected_mur, surface_val)
    st.success(f"Déperdition paroi Sud-Est : {dep:.3f} W")


#import streamlit as st

def calcul_dep_fenetre_Sud_Est():
    # Sélection du type de fenêtre
    choix_fenetre = st.selectbox(
        "Type de fenêtre (Sud-Est)",
        options=["Simple", "Double", "Fenetre double"],
        index=0
    )
    
    # Sélection du matériau de la fenêtre
    materiau = st.selectbox(
        "Matériaux de fenêtre (Sud-Est)",
        options=["Bois", "Metal"],
        index=0
    )
    
    # Saisie de la surface de la fenêtre (en m²)
    surface = st.number_input(
        "Surface de fenêtre (m²) (Sud-Est)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    st.write("Type choisi :", choix_fenetre)
    
    if choix_fenetre == "Simple":
        st.write("Vous avez choisi une fenêtre simple.")
        if materiau == "Bois":
            kwin = 5
        else:
            kwin = 5.8
    elif choix_fenetre == "Double":
        st.write("Vous avez choisi une fenêtre double.")
        # Sélection de l'épaisseur pour fenêtre double
        epaisseur = st.selectbox(
            "Choisissez l'épaisseur (mm) pour fenêtre double",
            options=["5 à 7", "8 à 9", "10 à 11", "12 à 13"],
            index=0
        )
        if materiau == "Bois":
            if epaisseur == "5 à 7":
                kwin = 3.3
            elif epaisseur == "8 à 9":
                kwin = 3.1
            elif epaisseur == "10 à 11":
                kwin = 3.0
            elif epaisseur == "12 à 13":
                kwin = 2.9
        else:
            if epaisseur == "5 à 7":
                kwin = 4.0
            elif epaisseur == "8 à 9":
                kwin = 3.9
            elif epaisseur == "10 à 11":
                kwin = 3.8
            elif epaisseur == "12 à 13":
                kwin = 3.7
    elif choix_fenetre == "Fenetre double":
        if materiau == "Bois":
            kwin = 2.6
        else:
            kwin = 3.0
    else:
        st.error("Type de fenêtre invalide.")
        return None
    
    st.write("kwin =", kwin)
    
    # Calcul de la résistance totale r et de la déperdition de la fenêtre
    r = (1 / kwin) + 0.025 + 0.03 + 0.16
    dep_fenetre = surface * (1 / r)
    return dep_fenetre

if st.button("Calculer déperdition de la fenêtre (Sud-Est)"):
    dep_value = calcul_dep_fenetre_Sud_Est()
    if dep_value is not None:
        st.write(f"Déperdition de la fenêtre (Sud-Est) : {dep_value:.3f}")



#import streamlit as st

def port_Sud_Est():
    # Sélection du type de contact du port
    choix_contact = st.selectbox(
        "Contact du port (Sud-Est)",
        options=["Exterieur", "Local Non Chauffé"],
        index=0
    )
    
    # Sélection du type de porte
    choix_port = st.selectbox(
        "Type de porte (Sud-Est)",
        options=[
            "Portes Opaques en Bois",
            "Portes Opaques en Metal",
            "Portes en Bois avec une proportion de vitrage <30%",
            "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
            "Portes en Metal equipées de vitrage simple"
        ],
        index=0
    )
    
    # Saisie de la surface du port (en m²)
    surface_port = st.number_input(
        "Surface du port (Sud-Est) (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )
    
    # Calcul du coefficient k_port_Sud_Est selon les choix
    if choix_contact == "Exterieur":
        if choix_port == "Portes Opaques en Bois":
            k_port = 3.5
        elif choix_port == "Portes Opaques en Metal":
            k_port = 5.8
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 4.0
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 4.5
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port = 5.8
    elif choix_contact == "Local Non Chauffé":
        if choix_port == "Portes Opaques en Bois":
            k_port = 2.0
        elif choix_port == "Portes Opaques en Metal":
            k_port = 4.5
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 2.4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 2.7
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port = 4.5
    else:
        k_port = 0

    st.write("k_port_Sud_Est =", k_port)
    
    dep_port = surface_port * k_port
    return dep_port

if st.button("Calculer déperdition du port Sud-Est"):
    dep_value = port_Sud_Est()
    st.write(f"Déperdition du port Sud-Est : {dep_value:.3f}")


#import streamlit as st

st.markdown("## Calcul de la Déperdition Transmission - Côté Sud-Est")

# Demander si le mur Sud-Est est présent (équivalent à var_Sud_Est.get() == 1)
mur_present = st.radio(
    "Le mur Sud-Est est-il présent ?",
    options=["Oui", "Non"],
    index=0
)

# Saisie de la surface du mur Sud-Est (m²)
surface_mur = st.number_input(
    "Surface du mur Sud-Est (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    key="surface_mur_sud_est"
)

# Définir des fonctions de calcul (exemple de simulation)
def calcul_dep_paroi_Sud_Est(surface):
    # Exemple : coefficient de 0.5 (à remplacer par votre calcul)
    return surface * 0.5

def calcul_dep_fenetre_Sud_Est():
    # Pour la simulation, on demande la surface des fenêtres
    surface_fenetre = st.number_input(
        "Surface des fenêtres Sud-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="surface_fenetre_sud_est"
    )
    # Exemple : coefficient de 0.3
    return surface_fenetre * 0.3

def port_Sud_Est():
    # Pour la simulation, on demande la surface des portes
    surface_port = st.number_input(
        "Surface des portes Sud-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="surface_port_sud_est"
    )
    # Exemple : coefficient de 0.4
    return surface_port * 0.4

# Calcul global de la déperdition de transmission côté Sud-Est
def calcul_dep_transmission_Sud_Est():
    if mur_present == "Oui":
        # Calcul de la déperdition de la paroi
        dep_paroi = calcul_dep_paroi_Sud_Est(surface_mur)
        
        # Vérifier si le mur est homogène
        mur_homogene = st.radio(
            "Le mur Sud-Est est-il homogène ?",
            options=["Oui", "Non"],
            index=0,
            key="homogene_sud_est"
        )
        
        if mur_homogene == "Oui":
            # Pour un mur homogène, on considère que la déperdition des fenêtres et portes est nulle
            dep_fenetre = 0
            dep_port = 0
            surface_fenetre_val = 0
            surface_port_val = 0
            s_mur = surface_mur
        else:
            # Pour un mur non homogène, on demande la surface des fenêtres et portes
            dep_fenetre = calcul_dep_fenetre_Sud_Est()
            dep_port = port_Sud_Est()
            s_mur = surface_mur
            # Ces valeurs seront réutilisées pour le calcul
            surface_fenetre_val = st.session_state.get("surface_fenetre_sud_est", 0.0)
            surface_port_val = st.session_state.get("surface_port_sud_est", 0.0)
        
        total_surface = s_mur + surface_fenetre_val + surface_port_val
        if total_surface > 0:
            dep_transmission = ((dep_paroi + dep_fenetre + dep_port) / total_surface) * s_mur
        else:
            dep_transmission = 0
        st.success(f"Déperdition transmission Sud-Est : {dep_transmission:.3f} W")
        return dep_transmission
    else:
        st.info("Déperdition transmission Sud-Est : 0.000 W")
        return 0

# Bouton pour lancer le calcul
if st.button("Calculer déperdition transmission Sud-Est"):
    calcul_dep_transmission_Sud_Est()

# Mise en page supplémentaire (section)
st.markdown("---")
st.markdown("### Section Sud-Est - Configuration détaillée")


#import streamlit as st

st.markdown("## Configuration du mur Sud-Est - Sélection et Homogénéité")

# Supposons que 'resistance_des_murs' est défini dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Sud-Est Exemple 1": (1.5, 200),
        "Mur Sud-Est Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur = st.selectbox(
    "Mur",
    options=["sélectionner"] + list(st.session_state.resistance_des_murs.keys())
)
st.write("Mur sélectionné :", selected_mur)

# Question sur l'orientation du mur Sud-Est
orientation = st.radio(
    "Y a-t-il un mur orienté vers le Sud-Est ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Orientation :", orientation)

# Question sur l'homogénéité du mur Sud-Est
homogene = st.radio(
    "Votre mur Sud-Est est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Homogénéité :", homogene)

# Si vous souhaitez déclencher une fonction de configuration en fonction du choix,
# vous pouvez utiliser une condition ici :
if homogene == "Oui":
    st.info("Configuration pour mur homogène activée.")
else:
    st.info("Configuration pour mur non homogène activée.")



#import streamlit as st

st.markdown("## Configuration du mur Sud-Est - Options avancées")

# Combobox pour choisir le mur déjà créé
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Sud-Est Exemple 1": (1.5, 200),
        "Mur Sud-Est Exemple 2": (2.0, 250)
    }
selected_mur = st.selectbox(
    "Mur",
    options=["sélectionner"] + list(st.session_state.resistance_des_murs.keys())
)
st.write("Mur sélectionné :", selected_mur)

# Question sur l'orientation du mur Sud-Est
orientation_sud_est = st.radio(
    "Y a-t-il un mur orienté vers le Sud-Est ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Orientation :", orientation_sud_est)

# Question sur l'homogénéité du mur Sud-Est
homogene_sud_est = st.radio(
    "Votre mur Sud-Est est-il Homogène ?",
    options=["Oui", "Non"],
    index=0
)
st.write("Homogénéité :", homogene_sud_est)

# Section pour la configuration de la fenêtre
st.markdown("### Configuration de la fenêtre")
surface_fenetre = st.number_input(
    "Surface totale de fenêtre (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
surface_mur = st.number_input(
    "Surface totale du mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
type_fenetre_options = ["Simple", "Double", "Fenetre double"]
type_fenetre = st.selectbox(
    "Type de fenêtre",
    options=type_fenetre_options,
    index=0
)
materiaux_fenetre = st.selectbox(
    "Matériaux de fenêtre",
    options=["Bois", "Metal"],
    index=0
)
epaisseur_options = ["5 à 7", "8 à 9", "10 à 11", "12 à 13", "cas de fenetre double"]
epaisseur = st.selectbox(
    "Épaisseur (mm)",
    options=epaisseur_options,
    index=0
)

# Section pour la configuration du port
st.markdown("### Configuration du port")
surface_port = st.number_input(
    "Surface totale de porte (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
contact_options = ["Exterieur", "Local Non Chauffé"]
contact_port = st.selectbox(
    "Contact avec",
    options=contact_options,
    index=0
)
materiau_port_options = [
    "Portes Opaques en Bois",
    "Portes Opaques en Metal",
    "Portes en Bois avec une proportion de vitrage <30%",
    "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
    "Portes en Metal equipées de vitrage simple"
]
materiau_port = st.selectbox(
    "Matériau de Porte",
    options=materiau_port_options,
    index=0
)


#import streamlit as st

st.markdown("## Configuration du mur Sud-Ouest")

# Demande si le mur Sud-Ouest est présent (équivalent à var_Sud_Ouest.get())
var_Sud_Ouest = st.radio(
    "Le mur Sud-Ouest est-il présent ?",
    options=["Oui", "Non"],
    index=0,
    key="var_Sud_Ouest"
)

if var_Sud_Ouest == "Oui":
    st.markdown("### Options pour mur Sud-Ouest")
    # Affichage des options pour homogénéité
    st.write("Votre mur Sud-Ouest est-il Homogène ?")
    homogene_option = st.radio(
        "Sélectionnez",
        options=["Oui", "Non"],
        index=0,
        key="homogene_Sud_Est"
    )
    st.write("Homogénéité sélectionnée :", homogene_option)
    
    # Simuler l'affichage de champs lorsque le mur est homogène
    if homogene_option == "Oui":
        st.write("Affichage des options pour mur homogène :")
        # Affichage de la surface totale du mur (similaire à lbl_surface_Sud_Est et entry_surface_Sud_Est)
        surface_mur = st.number_input("Surface totale du mur Sud-Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
        st.write("Surface du mur :", surface_mur, "m²")
        # Ici, on pourrait ajouter d'autres options spécifiques pour un mur homogène...
    else:
        st.write("Affichage des options pour mur non homogène :")
        # Affichage de la surface de fenêtre
        surface_fenetre = st.number_input("Surface totale de fenêtre Sud-Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
        # Affichage de la surface du mur
        surface_mur = st.number_input("Surface totale du mur Sud-Ouest (m²)", min_value=0.0, value=0.0, step=0.1)
        # Options pour le type de fenêtre et matériaux
        type_fenetre = st.selectbox("Type de fenêtre", options=["Simple", "Double", "Fenetre double"])
        materiaux_fenetre = st.selectbox("Matériaux de fenêtre", options=["Bois", "Metal"])
        st.write("Configuration non homogène activée avec :")
        st.write("- Surface de fenêtre :", surface_fenetre, "m²")
        st.write("- Surface du mur :", surface_mur, "m²")
        st.write("- Type de fenêtre :", type_fenetre)
        st.write("- Matériaux :", materiaux_fenetre)
else:
    st.markdown("### Options pour mur Sud-Ouest")
    st.write("Les options de configuration sont désactivées car le mur n'est pas présent.")


#import streamlit as st

st.markdown("## Configuration du mur Sud-Est - Homogénéité")

# Demander à l'utilisateur si le mur Sud-Est est homogène
homogene_sud_est = st.radio(
    "Votre mur Sud-Est est-il Homogène ?",
    options=["Oui", "Non"],
    index=0,
    key="homogene_sud_est"
)

if homogene_sud_est == "Oui":
    st.info("Configuration pour mur homogène activée.")
    # Pour un mur homogène, afficher uniquement les champs pour la surface totale du mur
    surface_mur_sud_est = st.number_input(
        "Surface totale du mur Sud-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="surface_mur_sud_est"
    )
    st.write("Surface du mur Sud-Est :", surface_mur_sud_est, "m²")
    # Ici, on n'affiche pas les champs pour fenêtres et autres options
else:
    st.info("Configuration pour mur non homogène activée.")
    # Pour un mur non homogène, afficher la saisie pour la surface des fenêtres et du mur
    surface_fenetre_sud_est = st.number_input(
        "Surface totale de fenêtre Sud-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="surface_fenetre_sud_est"
    )
    surface_mur_sud_est = st.number_input(
        "Surface totale du mur Sud-Est (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="surface_mur_sud_est_non_homogene"
    )
    # Affichage des options pour le vitrage et les matériaux
    type_fenetre_sud_est = st.selectbox(
        "Type de fenêtre Sud-Est",
        options=["Simple", "Double", "Fenetre double"],
        index=0,
        key="type_fenetre_sud_est"
    )
    materiaux_fenetre_sud_est = st.selectbox(
        "Matériaux de fenêtre Sud-Est",
        options=["Bois", "Metal"],
        index=0,
        key="materiaux_fenetre_sud_est"
    )
    # Affichage du récapitulatif des options
    st.write("Configuration non homogène activée avec les paramètres suivants :")
    st.write("- Surface fenêtre :", surface_fenetre_sud_est, "m²")
    st.write("- Surface mur :", surface_mur_sud_est, "m²")
    st.write("- Type de fenêtre :", type_fenetre_sud_est)
    st.write("- Matériaux de fenêtre :", materiaux_fenetre_sud_est)


#import streamlit as st

# On s'assure que le dictionnaire des murs est défini dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Sud-Ouest Exemple": (1.5, 200),
        "Mur Sud-Ouest Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

def calcul_dep_paroi_Sud_Ouest(selected_mur, surface):
    # Récupération des valeurs depuis le dictionnaire
    resistance, poid = resistance_des_murs[selected_mur]
    coef_k = 1 / resistance if resistance != 0 else 0
    dep_paroi = surface * coef_k
    # Masse de la paroi (calculée mais non utilisée ici)
    masse_paroi = surface * poid
    return dep_paroi

st.markdown("## Calcul de la déperdition de la paroi - Sud-Ouest")

# Widget pour sélectionner le mur
selected_mur = st.selectbox(
    "Sélectionnez le mur Sud-Ouest",
    options=list(resistance_des_murs.keys())
)

# Widget pour saisir la surface du mur (en m²)
surface = st.number_input(
    "Surface du mur Sud-Ouest (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

# Bouton pour lancer le calcul et afficher le résultat
if st.button("Calculer la déperdition de la paroi"):
    dep = calcul_dep_paroi_Sud_Ouest(selected_mur, surface)
    st.success(f"Déperdition de la paroi (Sud-Ouest) : {dep:.3f} W")



#import streamlit as st

def calcul_dep_fenetre_Sud_Ouest():
    # Sélection du type de fenêtre (équivalent de combo_type_fenetre_Sud_Ouest.get())
    choix_fenetre = st.selectbox(
        "Type de fenêtre Sud-Ouest",
        options=["Simple", "Double", "Fenetre double"],
        index=0,
        key="type_fenetre_sud_ouest"
    )
    
    # Sélection du matériau (équivalent de combo_materiaux_fenetre_Sud_Ouest.get())
    chois_materiaux = st.selectbox(
        "Matériaux de fenêtre Sud-Ouest",
        options=["Bois", "Metal"],
        index=0,
        key="materiaux_fenetre_sud_ouest"
    )
    
    # Saisie de la surface de fenêtre (équivalent de entry_surface_fenetre_Sud_Ouest.get())
    surface_fenetre = st.number_input(
        "Surface de fenêtre Sud-Ouest (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="surface_fenetre_sud_ouest"
    )
    
    st.write("Type de fenêtre choisi :", choix_fenetre)
    
    # Détermination de kwin_Sud_Ouest en fonction du type et du matériau
    if choix_fenetre == "Simple":
        st.write("Vous avez choisi une fenêtre simple.")
        if chois_materiaux == "Bois":
            kwin = 5
        else:
            kwin = 5.8
    elif choix_fenetre == "Double":
        st.write("Vous avez choisi une fenêtre double.")
        # Demande de l'épaisseur (équivalent de combo_epaisseur_aim_dair_Sud_Ouest.get())
        choix_epaisseur = st.selectbox(
            "Choisissez l'épaisseur (mm) pour fenêtre double",
            options=["5 à 7", "8 à 9", "10 à 11", "12 à 13"],
            index=0,
            key="epaisseur_sud_ouest"
        )
        if chois_materiaux == "Bois":
            if choix_epaisseur == "5 à 7":
                kwin = 3.3
            elif choix_epaisseur == "8 à 9":
                kwin = 3.1
            elif choix_epaisseur == "10 à 11":
                kwin = 3.0
            elif choix_epaisseur == "12 à 13":
                kwin = 2.9
        else:
            if choix_epaisseur == "5 à 7":
                kwin = 4.0
            elif choix_epaisseur == "8 à 9":
                kwin = 3.9
            elif choix_epaisseur == "10 à 11":
                kwin = 3.8
            elif choix_epaisseur == "12 à 13":
                kwin = 3.7
    elif choix_fenetre == "Fenetre double":
        st.write("Vous avez choisi Fenetre double.")
        if chois_materiaux == "Bois":
            kwin = 2.6
        else:
            kwin = 3.0
    else:
        st.error("Veuillez sélectionner un type de fenêtre valide.")
        return None

    st.write("kwin =", kwin)
    
    # Calcul de la résistance totale r et de la déperdition
    r = (1 / kwin) + 0.025 + 0.03 + 0.16
    dep_fenetre = surface_fenetre * (1 / r)
    return dep_fenetre

if st.button("Calculer déperdition fenêtre Sud-Ouest"):
    dep_value = calcul_dep_fenetre_Sud_Ouest()
    if dep_value is not None:
        st.success(f"Déperdition de la fenêtre Sud-Ouest : {dep_value:.3f}")


#import streamlit as st

def port_Sud_Ouest():
    # Sélection du type de contact du port (équivalent de combo_type_contacte_port_exterieur_Sud_Ouest.get())
    choix_contact = st.selectbox(
        "Contact du port (Sud-Ouest)",
        options=["Exterieur", "Local Non Chauffé"],
        index=0,
        key="contact_port_sud_ouest"
    )
    
    # Sélection du type de porte (équivalent de combo_type_port_exterieur_Sud_Ouest.get())
    choix_port = st.selectbox(
        "Type de porte (Sud-Ouest)",
        options=[
            "Portes Opaques en Bois",
            "Portes Opaques en Metal",
            "Portes en Bois avec une proportion de vitrage <30%",
            "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
            "Portes en Metal equipées de vitrage simple"
        ],
        index=0,
        key="type_port_sud_ouest"
    )
    
    # Saisie de la surface du port (équivalent de entry_surface_port_exterieur_Sud_Ouest.get())
    surface_port = st.number_input(
        "Surface du port (Sud-Ouest) (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="surface_port_sud_ouest"
    )
    
    # Calcul du coefficient k_port_Sud_Ouest selon les choix
    if choix_contact == "Exterieur":
        if choix_port == "Portes Opaques en Bois":
            k_port = 3.5
        elif choix_port == "Portes Opaques en Metal":
            k_port = 5.8
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 4.0
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 4.5
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port = 5.8
    elif choix_contact == "Local Non Chauffé":
        if choix_port == "Portes Opaques en Bois":
            k_port = 2.0
        elif choix_port == "Portes Opaques en Metal":
            k_port = 4.5
        elif choix_port == "Portes en Bois avec une proportion de vitrage <30%":
            k_port = 2.4
        elif choix_port == "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%":
            k_port = 2.7
        elif choix_port == "Portes en Metal equipées de vitrage simple":
            k_port = 4.5
    else:
        k_port = 0

    st.write("k_port_Sud_Ouest =", k_port)
    dep_port = surface_port * k_port
    return dep_port

if st.button("Calculer déperdition du port Sud-Ouest"):
    dep_value = port_Sud_Ouest()
    st.write(f"Déperdition du port Sud-Ouest : {dep_value:.3f}")


#import streamlit as st

# Dummy functions for demonstration purposes.
# Replace these with your actual implementations if available.
def calcul_dep_paroi_Sud_Est():
    # Saisie de la déperdition de la paroi (W)
    return st.number_input("Déperdition de la paroi Sud-Est (W)", min_value=0.0, value=0.0, step=0.1, key="dep_paroi_sud_est")

def calcul_dep_fenetre_Sud_Est():
    # Saisie de la déperdition de la fenêtre (W)
    return st.number_input("Déperdition de la fenêtre Sud-Est (W)", min_value=0.0, value=0.0, step=0.1, key="dep_fenetre_sud_est")

def port_Sud_Est():
    # Saisie de la déperdition du port (W)
    return st.number_input("Déperdition du port Sud-Est (W)", min_value=0.0, value=0.0, step=0.1, key="dep_port_sud_est")

def calcul_dep_transmission_Sud_Ouest():
    # Demander si le mur Sud-Ouest est présent
    mur_present = st.radio(
        "Le mur Sud-Ouest est-il présent ?",
        options=["Oui", "Non"],
        index=0,
        key="mur_present_sud_ouest"
    )
    if mur_present == "Oui":
        dep_paroi = calcul_dep_paroi_Sud_Est()
        
        # Demander si le mur est homogène
        mur_homogene = st.radio(
            "Le mur Sud-Ouest est-il homogène ?",
            options=["Oui", "Non"],
            index=0,
            key="homogene_sud_ouest"
        )
        if mur_homogene == "Oui":
            dep_fenetre = 0
            dep_port = 0
            surface_fenetre = 0
            surface_port = 0
            surface_mur = st.number_input("Surface du mur Sud-Ouest (m²)", min_value=0.0, value=0.0, step=0.1, key="surface_mur_sud_ouest")
        else:
            dep_fenetre = calcul_dep_fenetre_Sud_Est()
            dep_port = port_Sud_Est()
            surface_mur = st.number_input("Surface du mur Sud-Ouest (m²)", min_value=0.0, value=0.0, step=0.1, key="surface_mur_sud_ouest")
            surface_fenetre = st.number_input("Surface des fenêtres Sud-Ouest (m²)", min_value=0.0, value=0.0, step=0.1, key="surface_fenetre_sud_ouest")
            surface_port = st.number_input("Surface des portes Sud-Ouest (m²)", min_value=0.0, value=0.0, step=0.1, key="surface_port_sud_ouest")
        
        total_surface = surface_mur + surface_fenetre + surface_port
        if total_surface > 0:
            dep_transmission = ((dep_paroi + dep_fenetre + dep_port) / total_surface) * surface_mur
        else:
            dep_transmission = 0
        st.success(f"Déperdition transmission Sud-Ouest : {dep_transmission:.3f} W")
        return dep_transmission
    else:
        st.info("Déperdition transmission Sud-Ouest : 0.000 W")
        return 0

# Mise en page de la section Sud-Ouest (simulant lbl_frame_Sud_Ouest, etc.)
st.markdown("### Section Sud-Ouest - Configuration détaillée")
with st.container():
    st.markdown("#### Paramètres de transmission")
    if st.button("Calculer déperdition transmission Sud-Ouest"):
        calcul_dep_transmission_Sud_Ouest()


#import streamlit as st

st.markdown("## Configuration du mur Sud-Ouest - Sélection et Homogénéité")

# Supposons que le dictionnaire des murs est stocké dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Sud-Ouest Exemple 1": (1.5, 200),
        "Mur Sud-Ouest Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur = st.selectbox(
    "Mur",
    options=["sélectionner"] + list(st.session_state.resistance_des_murs.keys()),
    key="selected_mur_sud_ouest"
)
st.write("Mur sélectionné :", selected_mur)

# Radiobutton pour l'orientation vers le Sud-Ouest
orientation = st.radio(
    "Y a-t-il un mur orienté vers le Sud-Ouest ?",
    options=["Oui", "Non"],
    index=0,
    key="orientation_sud_ouest"
)
st.write("Orientation :", orientation)

# Radiobutton pour savoir si le mur est homogène
homogene = st.radio(
    "Votre mur Sud-Ouest est-il Homogène ?",
    options=["Oui", "Non"],
    index=0,
    key="homogene_sud_ouest"
)
st.write("Homogénéité :", homogene)

# Optionnel: Appel d'une fonction de configuration en fonction de la réponse
if homogene == "Oui":
    st.info("Configuration pour mur homogène activée.")
else:
    st.info("Configuration pour mur non homogène activée.")


#import streamlit as st

st.markdown("## Configuration du mur Sud-Ouest - Sélection et Homogénéité")

# Supposons que le dictionnaire des parois est stocké dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Sud-Ouest Exemple 1": (1.5, 200),
        "Mur Sud-Ouest Exemple 2": (2.0, 250)
    }

# Combobox pour choisir le mur déjà créé
selected_mur = st.selectbox(
    "Mur",
    options=["sélectionner"] + list(st.session_state.resistance_des_murs.keys()),
    key="mur_sud_ouest"
)
st.write("Mur sélectionné :", selected_mur)

# Radiobutton pour l'orientation vers le Sud-Ouest
orientation = st.radio(
    "Y a-t-il un mur orienté vers le Sud-Ouest ?",
    options=["Oui", "Non"],
    key="orientation_sud_ouest"
)
st.write("Orientation :", orientation)

# Radiobutton pour savoir si le mur est homogène
homogene = st.radio(
    "Votre mur Sud-Ouest est-il Homogène ?",
    options=["Oui", "Non"],
    key="homogene_sud_ouest"
)
st.write("Homogénéité :", homogene)

# Ici, vous pouvez appeler une fonction de configuration (par exemple, paroi_Sud_Ouest_homgene)
if homogene == "Oui":
    st.info("Configuration pour mur homogène activée.")
else:
    st.info("Configuration pour mur non homogène activée.")

st.markdown("## Configuration du port (Sud-Ouest)")

# Saisie de la surface totale de porte (m²)
surface_port = st.number_input(
    "Surface totale de porte (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    key="surface_port_sud_ouest"
)

# Sélection du type de contact du port
contact_options = ["Exterieur", "Local Non Chauffé"]
contact_port = st.selectbox(
    "Contact avec",
    options=contact_options,
    key="contact_port_sud_ouest"
)

# Sélection du matériau de porte
door_material_options = [
    "Portes Opaques en Bois",
    "Portes Opaques en Metal",
    "Portes en Bois avec une proportion de vitrage <30%",
    "Portes en Bois avec une proportion de vitrage compris entre 30% et 60%",
    "Portes en Metal equipées de vitrage simple"
]
materiau_port = st.selectbox(
    "Matériau de Porte",
    options=door_material_options,
    key="materiau_port_sud_ouest"
)


#import streamlit as st

st.markdown("## Configuration du plancher bas")

# Demander à l'utilisateur s'il souhaite activer la configuration du plancher bas
plancher_activation = st.radio(
    "Activez la configuration du plancher bas ?",
    options=["Oui", "Non"],
    index=0,
    key="plancher_activation"
)

if plancher_activation == "Oui":
    st.markdown("**Configuration activée (hauteur: 85)**")
    # Afficher deux options pour le plancher bas (similaire à deux boutons radio)
    option_plancher = st.radio(
        "Choisissez une option pour le plancher bas :",
        options=["Oui", "Non"],
        key="option_plancher"
    )
    st.write("Option choisie :", option_plancher)
else:
    st.markdown("**Configuration désactivée (hauteur: 60)**")
    st.write("Les options de configuration du plancher bas sont masquées.")


#import streamlit as st

st.markdown("## Configuration du plancher bas - Type de paroi")

# Simuler la variable var_type_plancher_bas_contacte via un radio button
option_type_plancher = st.radio(
    "Choisissez le type de contact pour le plancher bas:",
    options=["Option 1", "Option 2"],  # Option 1 correspond à 1, Option 2 à 2
    index=0,
    key="type_plancher_bas_contacte"
)

if option_type_plancher == "Option 1":
    st.markdown("### Configuration Option 1")
    # Affichage des widgets pour Option 1 :
    # Champ pour saisir la surface du plancher bas
    surface_plancher = st.number_input(
        "Surface totale du plancher bas (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="entry_surface_plancher_bas"
    )
    st.write("Surface du plancher :", surface_plancher, "m²")
    
    # Label indiquant le mur sélectionné
    st.markdown("**Mur**")
    # Combobox pour choisir le mur (simulé ici avec une liste d'exemples)
    murs = ["Mur A", "Mur B", "Mur C"]
    selected_mur = st.selectbox(
        "Choisissez le mur",
        options=murs,
        key="cmbol_plancher_bas"
    )
    st.write("Mur choisi :", selected_mur)
    
    # On simule l'affichage d'un conteneur avec des marges (pady, padx)
    st.markdown("---")
    st.write("Configuration Option 1 activée : affichage de la surface du mur et de la sélection du mur.")
    
elif option_type_plancher == "Option 2":
    st.markdown("### Configuration Option 2")
    # Affichage pour Option 2 :
    # Champ pour saisir la surface du plancher bas (position légèrement différente)
    surface_plancher = st.number_input(
        "Surface totale du plancher bas (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="entry_surface_plancher_bas_option2"
    )
    st.write("Surface du plancher :", surface_plancher, "m²")
    
    # On ne montre pas la combobox de sélection du mur dans cette option
    st.info("La sélection du mur est désactivée pour cette option.")
    
    st.markdown("---")
    st.write("Configuration Option 2 activée : affichage de la surface du mur seulement.")



#import streamlit as st

# Widgets de saisie pour la configuration du plancher bas

# Activation du plancher bas (similaire à var_Plancher_bas.get())
var_plancher = st.radio(
    "Activer le plancher bas ?",
    options=["Oui", "Non"],
    index=0,
    key="var_plancher_bas"
)

# Type de contact pour le plancher bas (similaire à var_type_plancher_bas_contacte.get())
# On suppose que "Option2" correspond à la valeur 2 dans l'ancien code.
type_contact = st.radio(
    "Type de contact pour le plancher bas",
    options=["Option1", "Option2"],
    index=0,
    key="type_plancher_bas_contacte"
)

# Saisie de la surface du plancher bas (similaire à entry_surface_Plancher_bas)
surface_plancher = st.number_input(
    "Surface du plancher bas (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    key="surface_plancher_bas"
)

# Si type de contact n'est pas "Option2", on demande de choisir un mur existant (similaire à cmbol_Plancher_bas)
selected_mur = st.selectbox(
    "Sélectionnez un mur pour le plancher bas",
    options=["Mur Exemple", "Mur Exemple 2"],
    key="cmbol_plancher_bas"
)

# On définit un dictionnaire de murs si non présent
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Exemple": (1.5, 200),
        "Mur Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

def calcul_dep_plancher_bas():
    if st.session_state.var_plancher_bas == "Oui":
        # Branche pour type de contact "Option2"
        if st.session_state.type_plancher_bas_contacte == "Option2":
            surface_val = st.session_state.surface_plancher_bas
            dep_paroi = surface_val * 1.75
            st.write(f"Déperdition plancher bas (Option2) : {dep_paroi:.3f} W")
            return dep_paroi
        else:
            # Branche utilisant la sélection d'un mur
            selected = st.session_state.cmbol_plancher_bas
            surface_val = st.session_state.surface_plancher_bas
            resistance, poid = resistance_des_murs[selected]
            coef_k = 1 / resistance if resistance != 0 else 0
            dep_paroi = surface_val * coef_k
            st.write(f"Déperdition plancher bas : {dep_paroi:.3f} W")
            return dep_paroi
    else:
        dep_paroi = 0
        st.write(f"Déperdition plancher bas : {dep_paroi:.3f} W")
        return dep_paroi

if st.button("Calculer déperdition du plancher bas"):
    calcul_dep_plancher_bas()



#import streamlit as st

# Fonction info pour afficher une fenêtre d'information (simulée)
def info():
    st.info(
        "Vous pouvez déterminer la valeur de Ks en vous basant sur les informations\n"
        "du fichier DTR C3.2/4, de la page 68 à la page 73."
    )

# Bouton pour afficher l'info
if st.button("Afficher Info"):
    info()

st.markdown("## Plancher Bas en Contact avec Le Sol")

# Simuler le cadre principal (lbl_frame_Plancher_bas)
with st.container():
    st.markdown("---")
    # Titre principal
    st.markdown("### Plancher Bas en Contact avec Le Sol")
    
    # Simuler le cadre interne principal (lbl_frame_interne_Plancher_bas)
    with st.container():
        # Afficher la question
        st.markdown("**Y a-t-il un Plancher en contact avec le Sol ?**")
        
        # Vous pouvez simuler les options de réponse en utilisant st.radio ou st.selectbox.
        # Ici, nous utilisons un radio pour simuler la réponse.
        reponse = st.radio(
            "Sélectionnez une option",
            options=["Oui", "Non"],
            key="plancher_contact"
        )
        st.write("Réponse sélectionnée :", reponse)
    
    # Simuler des cadres internes supplémentaires pour les options (lbl_frame_interne_Plancher_bas2, 3 et 4)
    with st.container():
        st.markdown("**Options supplémentaires (Frame 2)**")
        st.write("Ici, vous pouvez ajouter d'autres widgets de configuration pour le plancher bas.")
    
    with st.container():
        st.markdown("**Options supplémentaires (Frame 3)**")
        st.write("Ici, vous pouvez ajouter d'autres paramètres.")
    
    with st.container():
        st.markdown("**Options supplémentaires (Frame 4)**")
        st.write("Autres réglages optionnels pour le plancher bas.")



#import streamlit as st

st.markdown("## Configuration du plancher bas")

# Radiobutton pour l'orientation vers Plancher_bas
orientation_plancher = st.radio(
    "Le plancher bas est-il activé ?",
    options=["Oui", "Non"],
    key="var_plancher_bas"
)

# Radiobutton pour le type de contact du plancher bas
type_contact = st.radio(
    "Type de plancher bas",
    options=["Plancher haut enterré", "Plancher Bas et Mur enterré"],
    key="var_type_plancher_bas_contacte"
)

st.write("Orientation du plancher bas :", orientation_plancher)
st.write("Type de plancher bas :", type_contact)

# Selon le type de contact, afficher des champs différents
if type_contact == "Plancher haut enterré":
    st.markdown("### Configuration pour 'Plancher haut enterré'")
    # Saisie de la surface intérieure du plancher
    surface_plancher = st.number_input(
        "Surface intérieure de plancher (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="entry_surface_plancher_bas"
    )
    st.write("Surface saisie :", surface_plancher, "m²")
    
    # Combobox pour choisir le mur (simulé par une liste d'exemples)
    murs = ["Mur Exemple 1", "Mur Exemple 2"]
    selected_mur = st.selectbox(
        "Choisissez un mur",
        options=murs,
        key="cmbol_plancher_bas"
    )
    st.write("Mur sélectionné :", selected_mur)
else:
    st.markdown("### Configuration pour 'Plancher Bas et Mur enterré'")
    # Saisie de la surface intérieure du plancher
    surface_plancher = st.number_input(
        "Surface intérieure de plancher (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="entry_surface_plancher_bas_option2"
    )
    st.write("Surface saisie :", surface_plancher, "m²")
    st.info("La sélection du mur est désactivée pour cette option.")

# Option Info (bouton pour afficher des informations supplémentaires)
if st.button("Info"):
    st.info("Vous pouvez déterminer la valeur de Ks en vous basant sur les informations du fichier DTR C3.2/4, pages 68 à 73.")


#import streamlit as st

st.markdown("## Configuration du plancher terrasse")

# Demander si le plancher terrasse est activé (similaire à var_Plancher_Terrasse.get())
plancher_terrasse = st.radio(
    "Activez-vous le plancher terrasse ?",
    options=["Oui", "Non"],
    index=0,
    key="var_Plancher_Terrasse"
)

# Pour simplifier, nous utilisons du HTML pour simuler le comportement de pack/pack_forget et la configuration des hauteurs.
if plancher_terrasse == "Oui":
    st.markdown("### Configuration activée")
    # Ici, nous simulons l'affichage du cadre interne avec un padding spécifique (équivalent à pack(pady=(30, 5), padx=10, fill="x"))
    st.markdown(
        """
        <div style="border:1px solid #ccc; padding:30px 10px 5px 10px;">
            Contenu de configuration du plancher terrasse (affiché)
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown("### Configuration désactivée")
    # Simuler la disparition du cadre interne (équivalent à pack_forget) et réaffichage d'un autre cadre
    st.markdown(
        """
        <div style="border:1px solid #ccc; padding:30px 40px;">
            Contenu alternatif pour plancher terrasse (configuration désactivée)
        </div>
        """,
        unsafe_allow_html=True
    )


#import streamlit as st

# Simulation d'un dictionnaire de résistance pour les murs (à adapter selon vos données)
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Exemple 1": (1.5, 200),
        "Mur Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

st.markdown("## Plancher Terrasse - Configuration")

# Option pour activer le plancher terrasse (similaire à var_Plancher_Terrasse.get())
plancher_terrasse_active = st.radio(
    "Activez-vous le plancher terrasse ?",
    options=["Oui", "Non"],
    index=0,
    key="plancher_terrasse_active"
)

def calcul_dep_Plancher_Terrasse():
    if plancher_terrasse_active == "Oui":
        # Sélection du mur via une combobox (équivalent de cmbol_Plancher_Terrasse)
        choix_mur = st.selectbox(
            "Sélectionnez le mur pour le plancher terrasse",
            options=list(resistance_des_murs.keys()),
            key="cmbol_plancher_terrasse"
        )
        # Saisie de la surface du plancher terrasse (équivalent de entry_surface_Plancher_Terrasse)
        surface_plancher = st.number_input(
            "Surface du plancher terrasse (m²)",
            min_value=0.0,
            value=0.0,
            step=0.1,
            key="surface_plancher_terrasse"
        )
        # Récupération des paramètres du mur sélectionné
        resistance, poid = resistance_des_murs[choix_mur]
        coef_k = 1 / resistance if resistance != 0 else 0
        dep_transmission = surface_plancher * coef_k
        masse_paroi = surface_plancher * poid  # Calcul de la masse (non utilisé ici)
        st.success(f"Déperdition plancher terrasse : {dep_transmission:.3f} W")
        return dep_transmission
    else:
        dep_transmission = 0
        st.info(f"Déperdition plancher terrasse : {dep_transmission:.3f} W")
        return dep_transmission

# Mise en page simulant les frames
with st.container():
    st.markdown("---")
    st.markdown("### Plancher Terrasse en Contact avec le Sol")
    st.write("Ce qui suit simule l'interface pour configurer le plancher terrasse.")
    
    # Titre de la section
    st.markdown("**Plancher Terrasse en Contact avec Le Sol**")
    
    # Affichage de la question de configuration
    st.write("Y a-t-il un Plancher Terrasse ?")
    
    # Bouton pour lancer le calcul
    if st.button("Calculer déperdition plancher terrasse"):
        calcul_dep_Plancher_Terrasse()


#import streamlit as st

# Définissez votre fonction de callback (similaire à la commande "command=paroi_Plancher_Terrasse")
def paroi_Plancher_Terrasse():
    st.write("La fonction paroi_Plancher_Terrasse a été appelée.")

# Radiobutton pour l'orientation vers Plancher Terrasse (simulé via st.radio)
var_Plancher_Terrasse = st.radio(
    "Orientation vers Plancher Terrasse :",
    options=["Oui", "non"],
    index=0,
    key="var_Plancher_Terrasse"
)

# Dans Streamlit, le script se réexécute à chaque interaction.
# Vous pouvez appeler la fonction de callback en fonction de la sélection.
# Par exemple, on appelle la fonction chaque fois que le script est rechargé.
paroi_Plancher_Terrasse()


#import streamlit as st

st.markdown("## Configuration du plancher terrasse")

# On s'assure que le dictionnaire des murs existe dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur A": (1.5, 200),
        "Mur B": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

# Combobox pour choisir le mur déjà créé
st.markdown("**Mur**")
selected_mur = st.selectbox(
    "Sélectionnez un mur",
    options=["sélectionner"] + list(resistance_des_murs.keys()),
    key="cmbol_Plancher_Terrasse"
)
st.write("Mur sélectionné :", selected_mur)

# Saisie de la surface totale du plancher
st.markdown("**Surface Total de Plancher (m²)**")
surface_plancher = st.number_input(
    "Entrez la surface du plancher (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    key="entry_surface_Plancher_Terrasse"
)
st.write("Surface saisie :", surface_plancher, "m²")


#import streamlit as st

st.markdown("## Configuration du Local Non Chauffé")

# Demande si le local non chauffé est activé (similaire à var_local_non_chauffé.get())
var_local_non_chauffé = st.radio(
    "Local non chauffé :",
    options=["Oui", "Non"],
    index=0,
    key="local_non_chauffe"
)

# Si le local non chauffé est activé, afficher un conteneur avec des réglages spécifiques
if var_local_non_chauffé == "Oui":
    st.markdown("**Configuration activée :**")
    # Simuler la configuration de lbl_frame_interne_local_non_chauffé2 avec un padding
    st.markdown(
        """
        <div style="height:60px; padding:30px 10px 5px 10px; border:1px solid #ccc;">
            Contenu du local non chauffé (affiché)
        </div>
        """, 
        unsafe_allow_html=True
    )
else:
    st.markdown("**Configuration désactivée :**")
    # Simuler le masquage du conteneur interne et l'affichage d'un autre cadre (lbl_frame_local_non_chauffé)
    st.markdown(
        """
        <div style="height:60px; padding:30px 40px; border:1px solid #ccc;">
            Contenu alternatif du local non chauffé (affiché)
        </div>
        """, 
        unsafe_allow_html=True
    )


#import streamlit as st

st.markdown("## Local Non Chauffé - Configuration et Calcul")

# Simuler un dictionnaire de murs pour le local non chauffé
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Local Exemple 1": (1.5, 200),
        "Mur Local Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

# Titre de la section
st.markdown("### Local Non Chauffé")

# Question : Y a-t-il un Mur en contact avec un Local Non Chauffé ?
local_non_chauffe = st.radio(
    "Y a-t-il un Mur en contact avec un Local Non Chauffé ?",
    options=["Oui", "Non"],
    key="var_local_non_chauffe"
)
st.write("Réponse :", local_non_chauffe)

# Fonction de configuration (simulant paroi_local_non_chauffé)
def paroi_local_non_chauffé():
    st.info("Configuration du local non chauffé activée.")

# Si le local non chauffé est activé, on lance la configuration
if local_non_chauffe == "Oui":
    paroi_local_non_chauffé()
    
    # Sélection du mur (cmbol_local_non_chauffé)
    choix_mur = st.selectbox(
        "Sélectionnez le mur pour le local non chauffé",
        options=list(resistance_des_murs.keys()),
        key="cmbol_local_non_chauffe"
    )
    st.write("Mur sélectionné :", choix_mur)
    
    # Saisie de la surface du local non chauffé
    surface_local = st.number_input(
        "Surface du local non chauffé (m²)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="entry_surface_local_non_chauffe"
    )
    
    # Saisie des températures
    T_Tint = st.number_input(
        "Température intérieure (T_Tint)",
        min_value=-50.0, max_value=100.0,
        value=20.0, step=0.5,
        key="entry_Tint_local_non_chauffe"
    )
    T_esp = st.number_input(
        "Température extérieure non chauffée (T_esp)",
        min_value=-50.0, max_value=100.0,
        value=5.0, step=0.5,
        key="entry_T_esp_non_chauffe_local_non_chauffe"
    )
    T_Text = st.number_input(
        "Température extérieure (T_Text)",
        min_value=-50.0, max_value=100.0,
        value=0.0, step=0.5,
        key="entry_Text_local_non_chauffe"
    )
    
    def calcul_dep_local_non_chauffé():
        # Récupération des valeurs
        choix = st.session_state.cmbol_local_non_chauffe
        surface_val = float(st.session_state.entry_surface_local_non_chauffe)
        T_Tint_val = float(st.session_state.entry_Tint_local_non_chauffe)
        T_esp_val = float(st.session_state.entry_T_esp_non_chauffe_local_non_chauffe)
        T_Text_val = float(st.session_state.entry_Text_local_non_chauffe)
        
        # Récupération des paramètres du mur sélectionné
        resistance, poid = resistance_des_murs[choix]
        coef_k = 1 / resistance if resistance != 0 else 0
        
        # Calcul de Tau
        if (T_Tint_val - T_Text_val) != 0:
            Tau = (T_Tint_val - T_esp_val) / (T_Tint_val - T_Text_val)
        else:
            Tau = 0
        
        dep_transmission = Tau * (surface_val * coef_k)
        masse_paroi = surface_val * poid  # Calcul optionnel
        
        st.success(f"Déperdition transmission local non chauffé : {dep_transmission:.3f} W")
        return dep_transmission, Tau, surface_val, coef_k

    if st.button("Calculer déperdition local non chauffé"):
        calcul_dep_local_non_chauffé()
else:
    st.info("Local non chauffé désactivé.")

#import streamlit as st

st.markdown("## Configuration du Local Non Chauffé - Paramètres du Mur")

# Assurer que le dictionnaire des murs est défini dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur Exemple 1": (1.5, 200),
        "Mur Exemple 2": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

# Combobox pour choisir le mur déjà créé
st.markdown("**Sélection du mur**")
selected_mur = st.selectbox(
    "Mur",
    options=["sélectionner"] + list(resistance_des_murs.keys()),
    key="cmbol_local_non_chauffe"
)
st.write("Mur sélectionné :", selected_mur)

# Saisie de la surface intérieure du mur
st.markdown("**Surface intérieure de mur (m²)**")
surface_local = st.number_input(
    "Surface intérieure de mur (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    key="entry_surface_local_non_chauffe"
)
st.write("Surface saisie :", surface_local, "m²")

# Saisie de la température intérieure
st.markdown("**Température intérieure (°C)**")
Tint = st.number_input(
    "T intérieur (°C)",
    value=20.0,
    key="entry_Tint_local_non_chauffe"
)
st.write("T intérieur :", Tint, "°C")

# Saisie de la température de l'espace non chauffé
st.markdown("**Température de l'espace non chauffé (°C)**")
T_esp = st.number_input(
    "T espace Non Chauffé (°C)",
    value=5.0,
    key="entry_T_esp_non_chauffe_local_non_chauffe"
)
st.write("T espace Non Chauffé :", T_esp, "°C")

# Saisie de la température extérieure
st.markdown("**Température extérieure (°C)**")
Text = st.number_input(
    "T extérieur (°C)",
    value=0.0,
    key="entry_Text_local_non_chauffe"
)
st.write("T extérieur :", Text, "°C")



#import streamlit as st

def calcul_dep():
    # Ces fonctions doivent être définies ailleurs dans votre code Streamlit.
    # Ici, nous supposons qu'elles retournent des valeurs numériques.
    dep_transmission_nord = calcul_dep_transmission_nord()
    dep_transmission_sud = calcul_dep_transmission_sud()
    dep_transmission_est = calcul_dep_transmission_Est()
    dep_transmission_ouest = calcul_dep_transmission_ouest()
    dep_transmission_Nord_Est = calcul_dep_transmission_Nord_Est()
    dep_transmission_Nord_ouest = calcul_dep_transmission_Nord_ouest()
    dep_transmission_Sud_Est = calcul_dep_transmission_Sud_Est()
    dep_transmission_Sud_ouest = calcul_dep_transmission_Sud_ouest()
    dep_Plancher_Terrasse = calcul_dep_Plancher_Terrasse()
    dep_paroi_plancher_bas = calcul_dep_plancher_bas()
    (dep_transmision_local_non_chauffé, Tau,
     surface_local_non_chauffé, coef_k_local_non_chauffé) = calcul_dep_local_non_chauffé()

    # On calcule la déperdition totale sans local non chauffé
    deperdition_par_transmission_total = (
        dep_transmission_nord + dep_transmission_sud + dep_Plancher_Terrasse + dep_paroi_plancher_bas
    )
    # Ajout de la déperdition du local non chauffé
    deperdition_par_transmission_total_avec_lnc = deperdition_par_transmission_total + dep_transmision_local_non_chauffé
    # Calcul de la déperdition de liaison
    deperdition_par_transmission_liaison = 0.2 * deperdition_par_transmission_total_avec_lnc
    # Calcul final de la déperdition du local non chauffé
    dep_transmision_local_non_chauffé_final = Tau * ((surface_local_non_chauffé * coef_k_local_non_chauffé) + deperdition_par_transmission_liaison)
    # Calcul final de la déperdition totale avec un facteur de 1.2
    deperdition_par_transmission_total_final = (deperdition_par_transmission_total + dep_transmision_local_non_chauffé_final) * 1.2

    # Affichage des résultats
    st.write(f"Déperdition transmission local non chauffé : {dep_transmision_local_non_chauffé_final:.3f} W")
    st.write(f"Déperdition transmission liaison : {deperdition_par_transmission_liaison:.3f} W")
    st.write(f"Déperdition transmission totale finale : {deperdition_par_transmission_total_final:.3f} W")
    
    st.write("Déperdition transmission totale finale =", deperdition_par_transmission_total_final)
    return deperdition_par_transmission_total_final

# Bouton pour lancer le calcul global
if st.button("Calculer déperdition totale par transmission"):
    total_dep = calcul_dep()
    st.success(f"Déperdition totale par transmission : {total_dep:.3f} W")



#import streamlit as st

# Supposons que ces fonctions soient définies ailleurs dans votre application
def calcul_dep():
    st.write("Calcul de déperdition effectué.")
    # Placez ici votre logique de calcul
    return

def show_page(page):
    st.write(f"Navigation vers {page}")
    # Ici, vous pouvez implémenter la navigation entre vos pages,
    # par exemple en modifiant un paramètre de session ou en utilisant st.experimental_set_query_params
    return

def calcul_dep_show_pag_2():
    calcul_dep()
    show_page("page4")

st.markdown("## Navigation")

# Création d'un conteneur pour les boutons de navigation
with st.container():
    # Utilisation de colonnes pour aligner les boutons horizontalement
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Retour"):
            show_page("page2")
    with col2:
        if st.button("Suivant"):
            calcul_dep_show_pag_2()


#import streamlit as st

# Dictionnaires de valeurs
valeurs_P0 = {
    "Fenêtre ou porte-fenêtre": 4.0,
    "Porte avec seuil et joint d'étanchéité": 1.2,
    "Porte": 6.0,
    "Double fenêtre": 2.4
}

rugosite_dict = {
    "H (m)": ["H ≤ 4", "4 < H ≤ 7", "7 < H ≤ 11", "11 < H ≤ 18", "18 < H ≤ 30", "30 < H ≤ 50"],
    "centre des grandes villes": [0.40, 1.10, 1.76, 2.57, 3.50, 4.47],
    "zones urbaines ; zones industrielles ; forêts": [1.47, 2.30, 3.00, 3.87, 4.80, 5.78],
    "zones rurales avec arbres, haies, zones faiblement urbanisées": [2.71, 3.51, 4.19, 4.97, 5.80, 6.66],
    "rase campagne, aéroport": [4.06, 4.82, 5.46, 6.17, 6.93, 7.71],
    "bord de mer": [6.36, 7.08, 7.67, 8.32, 9.02, 9.72]
}

# Initialisation de la liste des parois dans st.session_state
if "entries" not in st.session_state:
    st.session_state.entries = []

# Fonction pour vérifier si une valeur peut être convertie en float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Fonction pour ajouter un type de paroi avec ses valeurs dans la liste
def ajouter_paroi():
    # Récupération des valeurs saisies dans les widgets
    type_paroi = st.session_state.type_var  # sélectionné via un selectbox
    nombre = st.session_state.entry_nombre   # saisi via un number_input (en tant qu'entier)
    surface = st.session_state.entry_surface   # saisi via un number_input (float)

    # Vérification que nombre est un entier et surface un float
    if str(nombre).isdigit() and is_float(surface):
        nombre = int(nombre)
        surface = float(surface)
        st.session_state.entries.append((type_paroi, nombre, surface))
        st.success(f"{nombre} x {type_paroi}, Surface : {surface} m² ajouté.")
    else:
        st.error("Erreur : Entrez des valeurs valides !")

st.markdown("### Ajouter un type de paroi")

# Widget pour sélectionner le type de paroi (on utilise les clés de valeurs_P0)
st.selectbox("Type de paroi", options=list(valeurs_P0.keys()), key="type_var")

# Widget pour saisir le nombre (nombre d'éléments)
st.number_input("Nombre", min_value=0, step=1, key="entry_nombre")

# Widget pour saisir la surface (en m²)
st.number_input("Surface (m²)", min_value=0.0, step=0.1, key="entry_surface")

# Bouton pour ajouter la paroi
if st.button("Ajouter paroi"):
    ajouter_paroi()

st.markdown("### Liste des parois ajoutées")
if st.session_state.entries:
    for entry in st.session_state.entries:
        type_paroi, nombre, surface = entry
        st.write(f"{nombre} x {type_paroi}, Surface : {surface} m²")
else:
    st.write("Aucune paroi ajoutée.")



#import streamlit as st

# Dictionnaires de valeurs
valeurs_P0 = {
    "Fenêtre ou porte-fenêtre": 4.0,
    "Porte avec seuil et joint d'étanchéité": 1.2,
    "Porte": 6.0,
    "Double fenêtre": 2.4
}

rugosite_dict = {
    "H (m)": ["H ≤ 4", "4 < H ≤ 7", "7 < H ≤ 11", "11 < H ≤ 18", "18 < H ≤ 30", "30 < H ≤ 50"],
    "centre des grandes villes": [0.40, 1.10, 1.76, 2.57, 3.50, 4.47],
    "zones urbaines ; zones industrielles ; forêts": [1.47, 2.30, 3.00, 3.87, 4.80, 5.78],
    "zones rurales avec arbres, haies, zones faiblement urbanisées": [2.71, 3.51, 4.19, 4.97, 5.80, 6.66],
    "rase campagne, aéroport": [4.06, 4.82, 5.46, 6.17, 6.93, 7.71],
    "bord de mer": [6.36, 7.08, 7.67, 8.32, 9.02, 9.72]
}

# Liste globale des parois ajoutées
if "entries" not in st.session_state:
    st.session_state.entries = []
entries = st.session_state.entries

# Widget pour saisir le volume (en m³)
volume = st.number_input("Volume (m³)", min_value=0.0, value=0.0, step=0.1, key="volume")

# Fonction qui calcule le débit total en fonction des parois ajoutées
def calculer_debit():
    """
    Calcule le débit total en fonction des parois ajoutées.
    Chaque entrée dans 'entries' est un tuple (type_paroi, nombre, surface).
    """
    debit_total = sum(nombre * valeurs_P0.get(type_paroi, 0) * surface 
                      for type_paroi, nombre, surface in entries)
    qv = 0.6 * float(volume)
    dr_final = 0.34 * (debit_total + qv)
    st.write(f"déperdition par renouvellement d'air : {dr_final:.2f} W/°C")
    st.write(f"Déperdition finale (entrée) : {dr_final:.3f}")
    return dr_final

# Fonction qui sélectionne la valeur de rugosité en fonction de la hauteur et du site d'implantation
def choix_ipm():
    h_selected = st.session_state.get("hauteur", "H ≤ 4")
    site_selected = st.session_state.get("site_implantation", "centre des grandes villes")
    if h_selected in rugosite_dict["H (m)"]:
        index = rugosite_dict["H (m)"].index(h_selected)
    else:
        index = 0
    st.write(f"Index de rugosité pour {h_selected} et {site_selected} : {index}")
    return index

# Fonction principale qui calcule et affiche les résultats
def calculer_dr():
    calculer_debit()
    choix_ipm()

# Fonction pour simuler la navigation vers la page 5 et lancer le calcul
def calculer_page_5():
    st.write("Navigation vers la page 5...")
    calculer_dr()

# Bouton pour déclencher le calcul et simuler le passage à la page 5
if st.button("Calculer et aller à la page 5"):
    calculer_page_5()

#import streamlit as st

st.markdown("## Ajout des fenêtres / Configuration du plancher terrasse")

# Supposons que le dictionnaire des murs est stocké dans st.session_state
if "resistance_des_murs" not in st.session_state:
    st.session_state.resistance_des_murs = {
        "Mur A": (1.5, 200),
        "Mur B": (2.0, 250)
    }
resistance_des_murs = st.session_state.resistance_des_murs

# Combobox pour choisir le mur déjà créé
st.markdown("### Sélection du mur")
selected_mur = st.selectbox(
    "Mur",
    options=["sélectionner"] + list(resistance_des_murs.keys()),
    key="cmbol_Plancher_Terrasse"
)
st.write("Mur sélectionné :", selected_mur)

# Saisie de la surface totale du plancher
st.markdown("### Surface totale du plancher")
surface_plancher = st.number_input(
    "Surface totale de plancher (m²)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    key="entry_surface_Plancher_Terrasse"
)
st.write("Surface saisie :", surface_plancher, "m²")


#import streamlit as st

# Dictionnaire de rugosité (exemple)
rugosite_dict = {
    "H (m)": ["H ≤ 4", "4 < H ≤ 7", "7 < H ≤ 11", "11 < H ≤ 18", "18 < H ≤ 30", "30 < H ≤ 50"],
    "centre des grandes villes": [0.40, 1.10, 1.76, 2.57, 3.50, 4.47],
    "zones urbaines ; zones industrielles ; forêts": [1.47, 2.30, 3.00, 3.87, 4.80, 5.78],
    "zones rurales avec arbres, haies, zones faiblement urbanisées": [2.71, 3.51, 4.19, 4.97, 5.80, 6.66],
    "rase campagne, aéroport": [4.06, 4.82, 5.46, 6.17, 6.93, 7.71],
    "bord de mer": [6.36, 7.08, 7.67, 8.32, 9.02, 9.72]
}

st.markdown("## Section Rugosité")

# Container for height selection (simulant un cadre)
with st.container():
    st.markdown("### Sélection de la hauteur")
    hauteur_selection = st.selectbox(
        "Sélectionner la hauteur",
        options=rugosite_dict["H (m)"],
        key="cmbol_Hauteur"
    )
    st.write("Hauteur sélectionnée :", hauteur_selection)

# Section pour le site d'implantation
st.markdown("### Site d'Implantation")
# Utiliser les clés du dictionnaire à partir du second élément (excluant "H (m)")
site_options = list(rugosite_dict.keys())[1:]
site_implantation = st.selectbox(
    "Site d'Implantation",
    options=site_options,
    key="cmbol_site_implantation"
)
st.write("Site d'Implantation sélectionné :", site_implantation)



#import streamlit as st

st.markdown("## Renouvellement d'Air et Navigation")

# --- Volume de Chambre ---
volume = st.number_input(
    "Volume de Chambre (m³)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    key="entry_volume"
)

# Affichage du résultat (simulant entry_depert_total)
result_label = st.empty()
result_label.text("déperdition par renouvellement d'air : 0.0 W/°C")

# --- Boutons de navigation ---
col1, col2 = st.columns(2)
with col1:
    if st.button("Retour", key="btn_to_page3"):
        st.write("Navigation vers la page précédente (page3)")
with col2:
    if st.button("Suivant", key="btm_calcul_dep"):
        st.write("Calcul et navigation vers la page suivante (page4)")
        # Ici, vous appelleriez votre fonction calculer_page_5() et mettre à jour le résultat.
        # Pour la démonstration, on met à jour le résultat avec une valeur fictive :
        result_label.text("déperdition par renouvellement d'air : 123.456 W/°C")

# --- Switch Mode Sombre ---
dark_mode = st.checkbox("Mode Sombre", value=False, key="switc4")
if dark_mode:
    st.write("Mode Sombre activé")
else:
    st.write("Mode Sombre désactivé")



#import streamlit as st

def get_temperature(zone, altitude):
    temp_ranges = {
        "A": [(300, 3), (450, 2), (600, 1), (800, 0), (float('inf'), -1.5)],
        "A1": [(300, 7), (450, 6), (600, 5), (800, 4), (float('inf'), 2.5)],
        "B": [(450, -2), (600, -3), (800, -4), (float('inf'), -5.5)],
        "C": [(300, 1), (450, 0), (600, -1), (800, -2), (float('inf'), -4.5)],
        "D": [(300, 4), (450, 3), (600, 2), (800, 1), (float('inf'), -0.5)]
    }

    if zone in temp_ranges:
        for limit, temp in temp_ranges[zone]:
            if altitude < limit:
                return temp
    return None

st.markdown("## Calcul de Température en fonction de l'Altitude")

# Sélection de la zone
zone = st.selectbox("Sélectionnez la zone", options=["A", "A1", "B", "C", "D"])

# Saisie de l'altitude
altitude = st.number_input("Altitude (m)", min_value=0.0, value=0.0, step=1.0)

# Calcul de la température basée sur la zone et l'altitude
temperature = get_temperature(zone, altitude)

if temperature is not None:
    st.success(f"Pour la zone {zone} et une altitude de {altitude} m, la température est de {temperature} °C.")
else:
    st.error("Aucune température trouvée pour ces paramètres.")


#import streamlit as st

# Dummy functions and variables to simulate the environment:
def get_temperature(zone, altitude):
    # Dummy implementation: returns a temperature based on zone and altitude.
    return 10.0

def calcul_dep():
    # Dummy implementation: returns total transmission loss (W)
    return 100.0

def calculer_debit():
    # Dummy implementation: returns the air renewal loss (W)
    return 20.0

# Coefficients (a, b, c, d, e) used in the comfort calculation
a, b, c, d, e = 0.5, 0.6, 0.7, 0.8, 0.9

# --- Widgets for inputs ---
choix_cr = st.selectbox(
    "Type de Chauffage (cr)",
    options=[
        "Chauffage Individuel",
        "chauffage central dans lesquelles toutes les tuyauteries sont calorifugées",
        "chauffage central dans lesquelles les tuyauteries sont calorifugées seulement dans les zones non chauffées",
        "chauffage central dont le réseau de tuyauteries n'est pas calorifugé."
    ]
)
choix_cin = st.selectbox(
    "Type de Chauffage Continu (cin)",
    options=[
        "Chauffage Continu",
        "chauffage discontinu, et dans le cas d'une construction dont la classe d'inertie est faible ou moyenne",
        "chauffage discontinu et dans le cas d'une construction dont la classe d'inertie est forte"
    ]
)
zonee = st.selectbox("Zone", options=["A", "B", "C", "D", "A1"])
altitudee = st.number_input("Altitude (m)", min_value=0.0, value=100.0, step=1.0)
tambia = st.number_input("Température Ambiante (°C)", value=20.0, step=0.5)
ts_ext = st.number_input("Température Externe (°C)", value=5.0, step=0.5)
sent_pln_bas = st.number_input("Sent Plancher Bas", value=2.0, step=0.1)
sent_mur = st.number_input("Sent Mur", value=3.0, step=0.1)
sent_port = st.number_input("Sent Porte", value=4.0, step=0.1)
sent_pf = st.number_input("Sent PF", value=1.0, step=0.1)

# --- Function: verification_confort ---
def verification_confort():
    # Determine cr based on choix_cr
    if choix_cr == "Chauffage Individuel":
        cr = 0
    elif choix_cr == "chauffage central dans lesquelles toutes les tuyauteries sont calorifugées":
        cr = 0.05
    elif choix_cr == "chauffage central dans lesquelles les tuyauteries sont calorifugées seulement dans les zones non chauffées":
        cr = 0.1
    elif choix_cr == "chauffage central dont le réseau de tuyauteries n'est pas calorifugé.":
        cr = 0.2
    else:
        cr = 0

    # Determine cin based on choix_cin
    if choix_cin == "Chauffage Continu":
        cin = 0.1
    elif choix_cin == "chauffage discontinu, et dans le cas d'une construction dont la classe d'inertie est faible ou moyenne":
        cin = 0.15
    elif choix_cin == "chauffage discontinu et dans le cas d'une construction dont la classe d'inertie est forte":
        cin = 0.2
    else:
        cin = 0

    st.write("cr =", cr)

    temperature_exterieur = get_temperature(zonee, altitudee)
    st.write(f"La température pour {zonee} à {altitudee} m est : {temperature_exterieur} °C")
    
    deperdition_total = calcul_dep()      # Total transmission loss
    dr_final = calculer_debit()            # Air renewal loss

    # Calculate dref using coefficients a, b, c, d, e and input values
    dref = (a * ts_ext) + (b * sent_pln_bas) + (c * sent_mur) + (d * sent_port) + (e * sent_pf)
    st.write(f"dref = {dref:.3f}")

    dtotaal = deperdition_total + dr_final
    if dtotaal <= 1.05 * dref:
        st.success("Votre logement est thermiquement confortable")
        conf_status = "confortable"
    else:
        st.error("Votre logement n'est pas thermiquement confortable")
        conf_status = "Non Confortable"

    # Calculate Q (heating power)
    Q = (tambia - temperature_exterieur) * ((1 + max(cr, cin)) * deperdition_total + ((1 + cr) * dr_final)) * 0.001
    st.write(f"La puissance de chauffage est = {Q:.3f} W")
    st.write(f"dref = {dref:.3f}")
    st.write(f"Puissance de chauffage (Q) = {Q:.3f}")
    
    return dref

# Bouton pour lancer la vérification de confort
if st.button("Vérifier le confort"):
    verification_confort()

st.markdown("## Fin de la vérification du confort")


#import streamlit as st

# Dummy implementations for demonstration.
# Remplacez ces fonctions par vos propres implémentations si nécessaire.
def show_page(page):
    st.write(f"Navigation vers {page}")

def verification_confort():
    st.write("Vérification du confort effectuée.")

def set_readonly():
    st.write("Les champs ont été mis en lecture seule.")

def final():
    show_page("page6")
    verification_confort()
    set_readonly()

if st.button("Finaliser"):
    final()



#import streamlit as st

# Titre de la page
st.markdown("<h2 style='text-align: center;'>Verification</h2>", unsafe_allow_html=True)

# Température Ambiante (°C)
st.markdown("### Température Ambiante (°C)")
temp_ambi = st.number_input("Température Ambiante (°C)", value=20.0, step=0.5, key="entry_temperature_Ambi")

# Mode d'Utilisation
st.markdown("### Mode d'Utilisation")
cincin = [
    "Chauffage Continu",
    "chauffage discontinu, et dans le cas d'une construction dont la classe d'inertie est faible ou moyenne",
    "chauffage discontinu et dans le cas d'une construction dont la classe d'inertie est forte"
]
mode_utilisation = st.selectbox("Mode d'Utilisation", options=cincin, key="combo_cin")

# Type de Chauffage
st.markdown("### Type de Chauffage")
crcr = [
    "Chauffage Individuel",
    "chauffage central dans lesquelles toutes les tuyauteries sont calorifugées",
    "chauffage central dans lesquelles les tuyauteries sont calorifugées seulement dans les zones non chauffées",
    "chauffage central dont le réseau de tuyauteries n'est pas calorifugé."
]
type_chauffage = st.selectbox("Type de Chauffage", options=crcr, key="combo_cr")

# Surfaces de la toiture (m²)
st.markdown("### Les surfaces de la toiture (m²)")
surface_toiture = st.number_input("Surface de la toiture (m²)", value=0.0, step=0.1, key="ent_ext")

# Surfaces de Plancher Bas (m²)
st.markdown("### Les surfaces de Plancher Bas\n(y compris les planchers bas sur locaux non chauffés)")
surface_plancher_bas = st.number_input("Surface de Plancher Bas (m²)", value=0.0, step=0.1, key="ent_pln_bas")

# Surfaces des murs (m²)
st.markdown("### Les surfaces des murs (m²)")
surface_mur = st.number_input("Surface des murs (m²)", value=0.0, step=0.1, key="ent_mur")

# Surfaces des portes (m²)
st.markdown("### Les surfaces des portes (m²)")
surface_portes = st.number_input("Surface des portes (m²)", value=0.0, step=0.1, key="ent_port")

# Surfaces des fenêtres et portes-fenêtres (m²)
st.markdown("### Les surfaces des fenêtres et portes-fenêtres (m²)")
surface_fenetres = st.number_input("Surface des fenêtres et portes-fenêtres (m²)", value=0.0, step=0.1, key="ent_pf")

# Boutons de navigation
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("Retour", key="btn_to_page4"):
        st.write("Navigation vers la page précédente (page4)")
with col2:
    if st.button("Calculer", key="btm_veri"):
        final()  # Assurez-vous que la fonction final() est définie ailleurs dans votre code



#import streamlit as st

# Supposons que ces widgets d'entrée ont été définis sur une page précédente et stockés dans st.session_state
# Vous pouvez les simuler ainsi pour le test :

if "entry_nom_projet" not in st.session_state:
    st.session_state.entry_nom_projet = st.text_input("Nom du projet", value="Projet Exemple", key="entry_nom_projet")
if "wilaya_var" not in st.session_state:
    st.session_state.wilaya_var = st.selectbox("Wilaya", options=["Wilaya1", "Wilaya2"], key="wilaya_var")
if "combo_zone" not in st.session_state:
    st.session_state.combo_zone = st.selectbox("Zone", options=["Zone1", "Zone2"], key="combo_zone")
if "ent_type_bati" not in st.session_state:
    st.session_state.ent_type_bati = st.selectbox("Type de bâtiment", options=["Maison", "Appartement"], key="ent_type_bati")
if "cmbol_site_implantation" not in st.session_state:
    st.session_state.cmbol_site_implantation = st.selectbox("Site d'implantation", options=["Site1", "Site2"], key="cmbol_site_implantation")

# Fonction pour transférer les informations vers la "page 6"
def transferer_informations():
    st.session_state.ent_nom_projet_dest = st.session_state.entry_nom_projet
    st.session_state.entry_wilaya_projet = st.session_state.wilaya_var
    st.session_state.entry_zone_projet = st.session_state.combo_zone
    st.session_state.entry_type_batiment = st.session_state.ent_type_bati
    st.session_state.entry_site_projet = st.session_state.cmbol_site_implantation
    st.success("Informations transférées vers la page 6.")

# Bouton pour transférer les informations
if st.button("Transférer les informations"):
    transferer_informations()

# Création du "frame principal" pour la page 6 (simulé par un conteneur)
st.markdown("## Informations du Projet (Page 6)")
with st.container():
    st.write("Nom du projet :", st.session_state.get("ent_nom_projet_dest", ""))
    st.write("Wilaya :", st.session_state.get("entry_wilaya_projet", ""))
    st.write("Zone :", st.session_state.get("entry_zone_projet", ""))
    st.write("Type de bâtiment :", st.session_state.get("entry_type_batiment", ""))
    st.write("Site d'implantation :", st.session_state.get("entry_site_projet", ""))


#import streamlit as st

st.markdown("## Information de Projet")
# Création de deux colonnes pour organiser l'interface
col_left, col_right = st.columns(2)

# COLONNE GAUCHE : Informations du projet
with col_left:
    st.markdown("### Information de Projet")
    nom_projet = st.text_input("Nom du projet", key="ent_nom_projet")
    wilaya_projet = st.text_input("Wilaya", key="entry_wilaya_projet")
    zone_projet = st.text_input("Zone", key="entry_zone_projet")
    type_batiment = st.text_input("Type de Bâtiment", key="entry_type_batiment")
    site_projet = st.text_input("Site d'Implantation", key="entry_site_projet")

# COLONNE DROITE : Calcul des Déperditions Thermiques et Autres Pertes
with col_right:
    st.markdown("### Calcul des Déperditions Thermiques")
    dep_nord = st.number_input("Déperdition Transmission Nord (W)", key="entry_depert_nord", value=0.0, step=0.1)
    dep_sud = st.number_input("Déperdition Transmission Sud (W)", key="entry_depert_sud", value=0.0, step=0.1)
    dep_est = st.number_input("Déperdition Transmission Est (W)", key="entry_depert_est", value=0.0, step=0.1)
    dep_ouest = st.number_input("Déperdition Transmission Ouest (W)", key="entry_depert_ouest", value=0.0, step=0.1)
    dep_nord_est = st.number_input("Déperdition Transmission Nord-Est (W)", key="entry_depert_nord_est", value=0.0, step=0.1)
    dep_nord_ouest = st.number_input("Déperdition Transmission Nord-Ouest (W)", key="entry_depert_nord_ouest", value=0.0, step=0.1)
    dep_sud_est = st.number_input("Déperdition Transmission Sud-Est (W)", key="entry_depert_sud_est", value=0.0, step=0.1)
    dep_sud_ouest = st.number_input("Déperdition Transmission Sud-Ouest (W)", key="entry_depert_sud_ouest", value=0.0, step=0.1)

    st.markdown("#### Autres pertes")
    dep_plancher_bas = st.number_input("Déperdition Transmission Plancher Bas (W)", key="entry_depert_plancher_bas", value=0.0, step=0.1)
    dep_plancher_haut = st.number_input("Déperdition Transmission Plancher Haut (W)", key="entry_depert_plancher_haut", value=0.0, step=0.1)
    dep_local_non_chauffe = st.number_input("Déperdition Transmission Local Non Chauffé (W)", key="entry_depert_local_non_chauffe", value=0.0, step=0.1)
    dep_liaison = st.number_input("Déperdition Transmission Liaison", key="entry_depert_liaison", value=0.0, step=0.1)
    dep_total = st.number_input("Déperdition Transmission Totale (W)", key="entry_depert_total", value=0.0, step=0.1)
    dr_final = st.number_input("Déperdition de renouvellement d'air (W/K)", key="entry_dr_final", value=0.0, step=0.1)
    dref = st.number_input("Déperdition de reference (W/°C)", key="entry_dref", value=0.0, step=0.1)
    Q = st.number_input("La Puissance de Chauffage (kW)", key="entry_Q", value=0.0, step=0.1)

st.markdown("---")
st.markdown("### Fin de la configuration")


#import streamlit as st

# Dummy functions to simulate page navigation
def show_page_verifie_1():
    st.write("Navigation vers la page de vérification...")

def show_page(page_name):
    st.write(f"Navigation vers {page_name}...")

# Fonction pour simuler le passage en mode readonly (affichage statique des valeurs)
def set_readonly():
    st.write("Les champs sont maintenant en lecture seule (simulation).")
    # Par exemple, vous pourriez afficher les valeurs dans des st.text_input avec disabled=True

# --- Bouton Suivant sur la page 1 ---
if st.button("Suivant", key="btn_to_page2"):
    show_page_verifie_1()

# Zone Label (simulé)
st.markdown("**Zone Label**")

# --- Bouton Retour sur la page 6 ---
if st.button("Retour", key="btn_to_page5"):
    show_page("page5")

# --- Bouton pour finaliser et mettre en readonly ---
if st.button("Finaliser et mettre en readonly", key="btn_set_readonly"):
    set_readonly()
