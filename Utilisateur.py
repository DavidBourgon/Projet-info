import pandas as pd


class Utilisateur:
    def __init__(self):
        pass

    def nombre_observation(self, data):
        """
        Compte le nombre d'observations dans un DataFrame.

        Args:
        data (DataFrame): Le DataFrame contenant les données.

        Returns:
        int: Nombre d'observations dans le DataFrame.

        Raises:
        TypeError: Si data n'est pas un DataFrame.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de nombre_observation "
                            "doit être un DataFrame.")

        return ("Nombre d'observations dans le DataFrame :", data.shape[0])

    def calcul_totaux_statut(self, data, statut):
        # statut est un str B pr bléssés
        # m mort
        # bm bléssés et mort
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de calcul_totaux"
                            " doit être un DataFrame.")

        elif statut == "B":
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            return ("Nombre total de personnes bléssées dans le tableau :",
                    total_persons_injuried)
        elif statut == "T":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            return ("Nombre total de personnes tuées dans le tableau :",
                    total_persons_killed)
        elif statut == "BT":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            total_both = total_persons_killed + total_persons_injuried
            return ("Nombre total d'individus bléssés et"
                    " tués dans le tableau :",
                    total_both)

    def calcul_type_statut(self, data, type, statut):
        """
        type str si auto / cycl / piet
        doit sortir un int
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de calcul_type_statut"
                            " doit être un DataFrame.")

        elif type == "Auto":
            colonnes_automobilistes = ["NUMBER.OF.MOTORIST.INJURED",
                                       "NUMBER.OF.MOTORIST.KILLED"]
            if statut == "B":
                total_automobilistes = data[colonnes_automobilistes[0]].sum()
                return ("Nombre total d'automobilistes blessés :",
                        total_automobilistes)
            elif statut == "T":
                total_automobilistes = data[colonnes_automobilistes[1]].sum()
                return ("Nombre total d'automobilistes tués :",
                        total_automobilistes)
            elif statut == "BT":
                total_automobilistes = data[colonnes_automobilistes].sum()\
                    .sum()
                return ("Nombre total d'automobilistes blessés tués :",
                        total_automobilistes)

        elif type == "Cycl":
            colonnes_cyclistes = ["NUMBER.OF.CYCLIST.INJURED",
                                  "NUMBER.OF.CYCLIST.KILLED"]
            if statut == "B":
                total_cyclistes = data[colonnes_cyclistes[0]].sum()
                return ("Nombre total de cyclistes blessés :",
                        total_cyclistes)
            elif statut == "T":
                total_cyclistes = data[colonnes_cyclistes[1]].sum()
                return ("Nombre total de cyclistes tués :",
                        total_cyclistes)
            elif statut == "BT":
                total_cyclistes = data[colonnes_cyclistes].sum().sum()
                return ("Nombre total de cyclistes blessés et tués :",
                        total_cyclistes)

        elif type == "Piet":
            colonnes_piétons = ["NUMBER.OF.PEDESTRIANS.INJURED",
                                "NUMBER.OF.PEDESTRIANS.KILLED"]
            if statut == "B":
                total_piétons = data[colonnes_piétons[0]].sum()
                return ("Nombre total de piétons blessés :",
                        total_piétons)
            elif statut == "T":
                total_piétons = data[colonnes_piétons[1]].sum()
                return ("Nombre total de piétons tués :",
                        total_piétons)
            elif statut == "BT":
                total_piétons = data[colonnes_piétons].sum().sum()
                return ("Nombre total de piétons blessés et tués :",
                        total_piétons)

    # fonction de filtres
    def filtrer_par_nom_de_rue(data, street):
        """
        Filtre le DataFrame en fonction du nom de la rue.

        Args:
        data (DataFrame): Le DataFrame contenant les données.
        street (str): Le nom de la rue à filtrer.

        Returns:
        DataFrame: Le DataFrame filtré contenant uniquement les lignes
        où le nom de la rue correspond à street.
        """
        # Filtrer le DataFrame en fonction du nom de la rue
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de filtrer_par_nom_de_rue"
                            " doit être un DataFrame.")

        filtered_data = data[data["CROSS.STREET.NAME"].str.contains(street) |
                             data["ON.STREET.NAME"].str.contains(street) |
                             data["OFF.STREET.NAME"].str.contains(street)]
        return ("Data frame filtré pour la rue dénomée:",
                street, filtered_data)

    def filtrer_par_date(self, data, date_debut, date_fin):
        """
        Filtre le DataFrame en fonction de la date entre date_debut
        et date_fin inclusivement.

        Args:
        data (DataFrame): Le DataFrame contenant les données.
        date_debut (str): La date de début de la période choisie au format
        "MM/DD/YYYY".
        date_fin (str): La date de fin de la période choisie au format
        "MM/DD/YYYY".

        Returns:
        DataFrame: Le DataFrame filtré.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de filtrer_par_date"
                            " doit être un DataFrame.")

        # Convertir les colonnes "CRASH.DATE" en type datetime
        data["CRASH_DATE"] = pd.to_datetime(data["CRASH.DATE"])

        # Les bornes sont prises
        filtered_data = data[(data["CRASH_DATE"] >= pd.to_datetime(date_debut))
                             &
                             (data["CRASH_DATE"] <= pd.to_datetime(date_fin))]

        # Supprimer la colonne temporaire "CRASH_DATE"
        filtered_data = filtered_data.drop(columns=["CRASH_DATE"])

        return ("Data frame filtré pour la période du",
                date_debut,
                "au",
                date_fin,
                filtered_data)

    def filtrer_par_heure(self, data, heure_debut, heure_fin):
        """
        Filtre le DataFrame en fonction de l'heure entre heure_debut
        et heure_fin inclusivement.

        Args:
        data (DataFrame): Le DataFrame contenant les données.
        heure_debut (str): L'heure de début de la période au format "HH:MM".
        heure_fin (str): L'heure de fin de la période au format "HH:MM".

        Returns:
        tuple: Un tuple contenant un message décrivant la période filtrée
        et le DataFrame filtré.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de filtrer_par_heure"
                            " doit être un DataFrame.")

        # Convertir les colonnes "CRASH.TIME" en type datetime
        data["CRASH_TIME"] = pd.to_datetime(data["CRASH.TIME"]).dt.\
            strftime("%H:%M")

        # Filtrer le DataFrame en fonction de l'heure entre heure_debut
        # et heure_fin inclusivement
        filtered_data = data[(data["CRASH_TIME"] >= heure_debut) &
                             (data["CRASH_TIME"] <= heure_fin)]

        # Supprimer la colonne temporaire "CRASH_TIME"
        filtered_data = filtered_data.drop(columns=["CRASH_TIME"])

        return ("Data frame filtré pour la période entre",
                heure_debut,
                "et",
                heure_fin, ":",
                filtered_data)

    def filtrer_par_modalité_variable(self, data, variable, modalite):
        """
        attention aussi à la variable qui doit être dans une liste de varible du tableau
        /!\ faire attention pour les vérification de type de madalité qui doit exister en utilisant la fonction est dans une liste de moadalités d'une variable
        Filtre le DataFrame en fonction d'une modalité spécifique d'une
        variable spécifique et renvoie le DataFrame filtré.

        Args:
        data (DataFrame): Le DataFrame contenant les données.
        modalité (str): La modalité spécifique à filtrer.

        Returns:
        DataFrame: Le DataFrame filtré.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de filtrer_par_modalité_variable"
                            " doit être un DataFrame.")

        filtered_data = data[data[variable] == modalite]
        return ("Data frame filtré pour la modalité",
                modalite,
                "de la variable",
                variable,
                filtered_data)

    # fonction listant les modalités et les variables d'un dataframe

    def liste_variables_dataframe(self, data):
        """
        Renvoie la liste des variables (colonnes) d'un DataFrame.

        Args:
        data (DataFrame): Le DataFrame contenant les données.

        Returns:
        list: Liste des variables (colonnes) du DataFrame.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de liste_variables_dataframe"
                            " doit être un DataFrame.")

        liste_variable = data.columns.tolist()
        return ("Liste des variables du DataFrame :",
                liste_variable)

    def liste_modalites_variable(self, data, variable):
        """
        Renvoie toutes les modalités différentes d'une variable
        dans une liste.

        attention varible en majusccule et séparéles mots par des points
        Args:
        data (DataFrame): Le DataFrame contenant les données.

        Returns:
        list: Liste des modalités différentes de la variable.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data de liste_modalites_variable"
                            " doit être un DataFrame.")

        liste_modalites = list(data[variable].unique())
        return ("Liste des modalités différentes de la variable :",
                variable, liste_modalites)
