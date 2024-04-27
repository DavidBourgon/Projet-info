import pandas as pd
import re


class Utilisateur:
    def nombre_observation(self, data):
        """
        Compte le nombre d'observations d'une base de données.

        Parameters
        ----------
        data : DataFrame
            La base de données dont on souhaite connaître le nombre
            d'observations.

        Returns
        -------
        Une liste dont le dernier élement est un
        int : Nombre d'observations de la base de données.

        Raises
        ------
        TypeError: Si data n'est pas un DataFrame.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        return ["Nombre d'observations dans la base de données :",
                data.shape[0]]

    def calcul_totaux_statut(self, data, statut):
        """
        Calcule le nombre de blessées et/ou de tués.

        data : DataFrame
            Base de données sur laquelle on veut déterminer le nombre de
            blessés et/ou tués.

        statut : str
            Statut des victimes.
            B : blessées
            T : tuées
            BT : blessées et tuées

        Returns
        -------
        Une liste dont le dernier élement est un
        int : Nombre de personnes blessées et/ou tuées selon le statut
              souhaité.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(statut, str):
            raise TypeError("Le statut doit être de type str.")

        if statut != "B" and statut != "T" and statut != "BT":
            raise ValueError("Le statut doit être B, T ou BT.")

        elif statut == "B":
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            return ["Nombre total de personnes blessées dans le tableau :",
                    total_persons_injuried]
        elif statut == "T":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            return ["Nombre total de personnes tuées dans le tableau :",
                    total_persons_killed]
        elif statut == "BT":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            total_both = total_persons_killed + total_persons_injuried
            return ["Nombre total d'individus blessés et"
                    " tués dans le tableau :",
                    total_both]

    def calcul_totaux_cat_statut(self, data, cat, statut):
        """
        Calcule le nombre de blessées et/ou de tués selon le type de personnes
        souhaité.

        data : DataFrame
            Base de données sur laquelle on veut déterminer le nombre de
            blessés et/ou tués.

        cat : str
            Catégorie des personnes dont on veut déterminer le nombre
            de blessés et/ou tués.
            auto : automobilistes
            cycl : cyclistes
            piet : piétons

        statut : str
            Statut des victimes.
            B : blessées
            T : tuées
            BT : blessées et tuées

        Returns
        -------
        Une liste dont le dernier élement est un
        int : Nombre de personnes blessées et/ou tuées selon le type et le
              statut souhaités.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(statut, str):
            raise TypeError("Le statut doit être de type str.")

        if statut != "B" and statut != "T" and statut != "BT":
            raise ValueError("Le statut doit être B, T ou BT.")

        if not isinstance(cat, str):
            raise TypeError("L'état doit être de type str.")

        if cat != "cycl" and cat != "auto" and cat != "piet":
            raise ValueError("L'état doit être auto, cycl ou piet.")

        elif cat == "auto":
            colonnes_automobilistes = ["NUMBER.OF.MOTORIST.INJURED",
                                       "NUMBER.OF.MOTORIST.KILLED"]
            if statut == "B":
                total_automobilistes = data[colonnes_automobilistes[0]].sum()
                return ["Nombre total d'automobilistes blessés :",
                        total_automobilistes]
            elif statut == "T":
                total_automobilistes = data[colonnes_automobilistes[1]].sum()
                return ["Nombre total d'automobilistes tués :",
                        total_automobilistes]
            elif statut == "BT":
                total_automobilistes = data[colonnes_automobilistes].sum()\
                    .sum()
                return ["Nombre total d'automobilistes blessés et tués :",
                        total_automobilistes]

        elif cat == "cycl":
            colonnes_cyclistes = ["NUMBER.OF.CYCLIST.INJURED",
                                  "NUMBER.OF.CYCLIST.KILLED"]
            if statut == "B":
                total_cyclistes = data[colonnes_cyclistes[0]].sum()
                return ["Nombre total de cyclistes blessés :",
                        total_cyclistes]
            elif statut == "T":
                total_cyclistes = data[colonnes_cyclistes[1]].sum()
                return ["Nombre total de cyclistes tués :",
                        total_cyclistes]
            elif statut == "BT":
                total_cyclistes = data[colonnes_cyclistes].sum().sum()
                return ["Nombre total de cyclistes blessés et tués :",
                        total_cyclistes]

        elif cat == "piet":
            colonnes_piétons = ["NUMBER.OF.PEDESTRIANS.INJURED",
                                "NUMBER.OF.PEDESTRIANS.KILLED"]
            if statut == "B":
                total_piétons = data[colonnes_piétons[0]].sum()
                return ["Nombre total de piétons blessés :",
                        total_piétons]
            elif statut == "T":
                total_piétons = data[colonnes_piétons[1]].sum()
                return ["Nombre total de piétons tués :",
                        total_piétons]
            elif statut == "BT":
                total_piétons = data[colonnes_piétons].sum().sum()
                return ["Nombre total de piétons blessés et tués :",
                        total_piétons]

    # fonction de filtres
    def filtrer_par_nom_de_rue(data, street):
        """
        Filtre la base de données en fonction de la rue souhaitée.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        street : str
            Le nom de la rue selon laquelle nous souhaitons filtrer la base de
            données.

        Returns
        -------
        Une liste dont le dernier élement est un
        DataFrame : La base de données filtrée contenant uniquement les lignes
                    où le nom de la rue correspond à street.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(street, str):
            raise TypeError("Le nom de la rue doit être de type str.")

        # ici faire qqch pr bien voir que street existe et que ça a du sens
        # de dire qu'il contient il faudrait faire une fonction annexe
        # Pour que cela soit propre
        filtered_data = data[data["CROSS.STREET.NAME"].str.contains(street) |
                             data["ON.STREET.NAME"].str.contains(street) |
                             data["OFF.STREET.NAME"].str.contains(street)]
        return ["Base de données filtrée pour la rue nomée:",
                street, filtered_data]

    def filtrer_par_date(self, data, date_debut, date_fin):
        """
        Filtre le DataFrame en fonction de la date entre date_debut
        et date_fin inclus.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        date_debut : str
            La date de début de la période choisie au format "MM/DD/YYYY".

        date_fin : str
            La date de fin de la période choisie au format "MM/DD/YYYY".

        Returns
        -------
        Une liste dont le dernier élement est un
        DataFrame : Le base de données filtrée.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(date_debut, str):
            raise TypeError("La date début doit être un str.")

        if not re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/[0-9]{4}$',
                        date_debut):
            raise ValueError("La date début doit être au format 'MM/JJ/AAAA'.")

        if not isinstance(date_fin, str):
            raise TypeError("La date fin doit être un str.")

        if not re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/[0-9]{4}$',
                        date_fin):
            raise ValueError("La date fin doit être au format 'MM/JJ/AAAA'.")

        # Convertir les colonnes "CRASH.DATE" en type datetime
        data["CRASH_DATE"] = pd.to_datetime(data["CRASH.DATE"])

        # Les bornes sont prises
        filtered_data = data[(data["CRASH_DATE"] >= pd.to_datetime(date_debut))
                             &
                             (data["CRASH_DATE"] <= pd.to_datetime(date_fin))]

        # Supprimer la colonne temporaire "CRASH_DATE"
        filtered_data = filtered_data.drop(columns=["CRASH_DATE"])

        return ["Base de données filtrée pour la période du",
                date_debut,
                "au",
                date_fin,
                filtered_data]

    def filtrer_par_heure(self, data, heure_debut, heure_fin):
        """
        Filtre le DataFrame en fonction de l'heure entre heure_debut
        et heure_fin inclus.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        heure_debut : str
            L'heure de début de la période au format "HH:MM".

        heure_fin : str
            L'heure de fin de la période au format "HH:MM".

        Returns
        -------
        list : Une liste contenant un message décrivant la période filtrée
            et le DataFrame filtré.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(heure_debut, str):
            raise TypeError("L'heure de début doit être un str")

        if not re.match(r'^(2[0-3]|[01][0-9]):[0-5][0-9]$', heure_debut):
            raise ValueError("L'heure de début doit être au format 'HH:MM'.")

        if not isinstance(heure_debut, str):
            raise TypeError("L'heure de fin doit être un str")

        if not re.match(r'^(2[0-3]|[01][0-9]):[0-5][0-9]$', heure_debut):
            raise ValueError("L'heure de fin doit être au format 'HH:MM'.")

        # Convertir les colonnes "CRASH.TIME" en type datetime
        data["CRASH_TIME"] = pd.to_datetime(data["CRASH.TIME"]).dt.\
            strftime("%H:%M")

        # Filtrer le DataFrame en fonction de l'heure entre heure_debut
        # et heure_fin inclusivement
        filtered_data = data[(data["CRASH_TIME"] >= heure_debut) &
                             (data["CRASH_TIME"] <= heure_fin)]

        # Supprimer la colonne temporaire "CRASH_TIME"
        filtered_data = filtered_data.drop(columns=["CRASH_TIME"])

        return ["Base de données filtrée pour la période entre",
                heure_debut,
                "et",
                heure_fin, ":",
                filtered_data]

    def filtrer_par_modalite_variable(self, data, variable, modalite):
        """
        Filtre la base de données en fonction d'une modalité spécifique d'une
        variable spécifique et renvoie la base de données filtrée.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        variable : str
            La variable spécifique à filtrer.

        modalite : str
            La modalité spécifique à filtrer.

        Returns
        -------

        Une liste dont le dernier élement est un
        DataFrame : La base de données filtrée.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if variable not in self.liste_variables_dataframe(data)[-1]:
            raise ValueError("Cette variable n'est pas dans la base de "
                             "données.")

        if not isinstance(modalite, str):
            raise TypeError("La modalité doit être de type str.")

        if modalite not in self.liste_modalites_variable(data, variable)[-1]:
            raise ValueError("Cette modalité n'existe pas pour la variable "
                             "choisie.")

        filtered_data = data[data[variable] == modalite]
        return ["Base de données filtrée pour la modalité",
                modalite,
                "de la variable",
                variable,
                filtered_data]

    # fonction listant les modalités et les variables d'un dataframe

    def liste_variables_dataframe(self, data):
        """
        Renvoie la liste des variables (colonnes) d'une base de données.

        Parameters
        ----------
        data : DataFrame
            La base de données dont on souhaite la liste des variables.

        Returns
        -------
        list : Liste des variables (colonnes) de la base de données.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        liste_variable = data.columns.tolist()
        return ["Liste des variables de la base de données :",
                liste_variable]

    def liste_modalites_variable(self, data, variable):
        """
        Renvoie toutes les modalités différentes d'une variable d'une base de
        données.

        attention varible en majuscule et séparer les mots par des points

        Parameters
        ----------
        data : DataFrame
            La base de données dont on souhaite obtenir les modalités d'une de
            ses variables.

        variable : str
            Variable dont on souhaite obtenir toutes les modalités.

        Returns
        -------
        list : Liste des modalités différentes de la variable.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(variable, str):
            raise TypeError("La variable doit être de type str.")

        if not re.match(r'^[A-Z0-9.]+$', variable):
            raise ValueError("La variable ne doit contenir que "
                             "des majuscules, des points, des nombres "
                             "et pas d'espace.")

        if variable not in self.liste_variables_dataframe(data)[-1]:
            raise ValueError("Cette variable n'est pas dans la base de "
                             "données.")

        liste_modalites = list(data[variable].unique())
        return ["Liste des modalités différentes de la variable :",
                variable, liste_modalites]

    # fonction avancée
    def danger_rue(self, data, street, cat):
        data_street = self.filtrer_par_nom_de_rue(data, street)[-1]
        n_tot = self.nombre_observation(data)[-1]
        if n_tot == 0:
            return ["Il n'y a pas d'accidents ou bien le tableau est vide.",
                    "Pour la rue :", street,
                    "Il y a un rique (en %) de :", 0]
        else:
            n_T = self.calcul_totaux_cat_statut(data_street, cat, "T")[-1]
            n_B = self.calcul_totaux_cat_statut(data_street, cat, "B")[-1]
            risque = (n_T + (1/4)*n_B) / n_tot
            return ["Pour la rue :", street,
                    "et la catégorie d'usagée", cat,
                    "il y a un rique (en %) de :", risque]
