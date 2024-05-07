import pandas as pd
import re


class Utilisateur:
    @staticmethod
    def nombre_observation(data):
        """
        Compte le nombre d'observations d'une base de données.

        Parameters
        ----------
        data : DataFrame
            La base de données dont on souhaite connaître le nombre
            d'observations.

        Returns
        -------
        list : Phrase réponse avec le nombre d'observations de la base de
               données.

        Raises
        ------
        TypeError: Si data n'est pas un DataFrame.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        return ["Nombre d'observations dans la base de données :",
                data.shape[0]]

    def calcul_totaux_statut(data, statut):
        """
        Calcule le nombre de blessés et/ou de tués.

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
        list : Liste contenant une phrase réponse et le nombre de personnes
            blessées et/ou tuées selon le statut souhaité.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(statut, str):
            raise TypeError("Le statut doit être de type str.")

        if statut != "B" and statut != "T" and statut != "BT":
            raise ValueError("Le statut doit être B, T ou BT.")

        elif statut == "B":
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            return ["Nombre total d'individus blessés :",
                    total_persons_injuried]
        elif statut == "T":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            return ["Nombre total d'individus tués :",
                    total_persons_killed]
        elif statut == "BT":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            total_both = total_persons_killed + total_persons_injuried
            return ["Nombre total d'individus blessés et tués :",
                    total_both]

    def calcul_totaux_cat_statut(data, categorie, statut):
        """
        Calcule le nombre de blessés et/ou de tués selon le type de personnes
        souhaité.

        data : DataFrame
            Base de données sur laquelle on veut déterminer le nombre de
            blessés et/ou tués.

        categorie : str
            Catégorie des personnes dont on veut déterminer le nombre
            de blessés et/ou tués.
            car : automobilistes
            cycle : cyclistes
            foot : piétons

        statut : str
            Statut des victimes.
            B : blessées
            T : tuées
            BT : blessées et tuées

        Returns
        -------
        list : Liste contenant une phrase réponse et le nombre de personnes
            blessées et/ou tuées selon la catégorie souhaitée et le statut
            souhaité.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(statut, str):
            raise TypeError("Le statut doit être de type str.")

        if statut != "B" and statut != "T" and statut != "BT":
            raise ValueError("Le statut doit être B, T ou BT.")

        if not isinstance(categorie, str):
            raise TypeError("La catégorie doit être de type str.")

        if categorie != "cycle" and categorie != "car" and categorie != "foot":
            raise ValueError("La catégorie doit être car, cycle ou foot.")

        elif categorie == "car":
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

        elif categorie == "cycle":
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

        elif categorie == "foot":
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
        list : Une liste contenant un message donnant la rue choisie et le
            DataFrame filtré

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(street, str):
            raise TypeError("Le nom de la rue doit être de type str.")

        filtered_data = data[data["CROSS.STREET.NAME"].str.contains(street) |
                             data["ON.STREET.NAME"].str.contains(street) |
                             data["OFF.STREET.NAME"].str.contains(street)]
        return ["Base de données filtrée pour la rue nomée:",
                street, filtered_data]

    def filtrer_par_date(data, date_debut, date_fin):
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
        list : Une liste contenant un message décrivant la période filtrée
            et le DataFrame filtré entre le jour de début et de fin de
            la période.

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

        if date_debut > date_fin:
            raise ValueError("La date de début ne doit pas être supérieure"
                             " à la date de fin.")

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

    def filtrer_par_heure(data, heure_debut, heure_fin):
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

        # Ne prends pas 24h00 mais prend 00:00

        if not re.match(r'^(2[0-3]|[01][0-9]):[0-5][0-9]$', heure_debut):
            raise ValueError("L'heure de début doit être au format 'HH:MM'.")

        if not isinstance(heure_fin, str):
            raise TypeError("L'heure de fin doit être un str")

        if not re.match(r'^(2[0-3]|[01][0-9]):[0-5][0-9]$', heure_fin):
            raise ValueError("L'heure de fin doit être au format 'HH:MM'.")

        if heure_debut > heure_fin:
            raise ValueError("L'heure de début ne doit pas être supérieure"
                             " à l'heure de fin.")

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

    def filtrer_par_modalite_variable(data, modalite, variable):
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
        list : Une liste contenant un message décrivant la modalité filtrée
               d'une certaine variable et le DataFrame filtré.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if variable not in Utilisateur.liste_variables_dataframe(data)[-1]:
            raise ValueError("Cette variable n'est pas dans la base de "
                             "données.")

        L_mod_var = Utilisateur.liste_modalites_variable(data, variable)[-1]
        if modalite not in L_mod_var:
            raise ValueError("Cette modalité n'existe pas pour la variable "
                             "choisie.")

        filtered_data = data[data[variable] == modalite]
        return ["Base de données filtrée pour la modalité",
                modalite,
                "de la variable",
                variable,
                filtered_data]

    # fonction listant les modalités et les variables d'un dataframe

    def liste_variables_dataframe(data):
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

    def liste_modalites_variable(data, variable):
        """
        Renvoie toutes les modalités différentes d'une variable d'une base de
        données.

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

        List_Variables = Utilisateur.liste_variables_dataframe(data)
        if variable not in List_Variables[-1]:
            raise ValueError("Cette variable n'est pas dans la base de "
                             "données.")

        liste_modalites = list(data[variable].astype(str).unique())
        return ["Liste des modalités différentes de la variable :",
                variable, liste_modalites]

    def df_blesse_mort_rue(data, categorie):
        data.dropna(subset=["CONTRIBUTING.FACTOR.VEHICLE.1"], inplace=True)
        data["NUMBER.OF.PERSONS.INJURED"] = data["NUMBER.OF.PERSONS.INJURED"].fillna(0)
        data["NUMBER.OF.PERSONS.KILLED"] = data["NUMBER.OF.PERSONS.KILLED"].fillna(0)

        rues = pd.unique(pd.concat([data["ON.STREET.NAME"],
                                    data["OFF.STREET.NAME"],
                                    data["CROSS.STREET.NAME"]]))    
        nombre_blesses_pietons_par_rue = {}
        nombre_blesses_cyclistes_par_rue = {}
        nombre_tues_pietons_par_rue = {}
        nombre_tues_cyclistes_par_rue = {}
    
        for rue in rues:
            rue_filtre = data[(data["ON.STREET.NAME"] == rue) |
                              (data["OFF.STREET.NAME"] == rue) |
                              (data["CROSS.STREET.NAME"] == rue)]        
            if categorie == "foot":
                total_blesses_pietons = \
                    Utilisateur.calcul_totaux_cat_statut(rue_filtre, categorie, "B")[-1]
                total_tues_pietons = \
                    Utilisateur.calcul_totaux_cat_statut(rue_filtre, categorie, "T")[-1]
                nombre_blesses_pietons_par_rue[rue] = total_blesses_pietons
                nombre_tues_pietons_par_rue[rue] = total_tues_pietons
            elif categorie == "cycle":
                total_blesses_cyclistes = \
                    Utilisateur.calcul_totaux_cat_statut(rue_filtre, categorie, "B")[-1]
                total_tues_cyclistes = \
                    Utilisateur.calcul_totaux_cat_statut(rue_filtre, categorie, "B")[-1]
                nombre_blesses_cyclistes_par_rue[rue] = total_blesses_cyclistes
                nombre_tues_cyclistes_par_rue[rue] = total_tues_cyclistes

        df_result = None
        if categorie == "foot":
            df_pietons = pd.DataFrame(list(
                nombre_blesses_pietons_par_rue.items()),
                    columns=["Rue", "Nombre blesses pietons"])
            df_tues_pietons = pd.DataFrame(list(
                nombre_tues_pietons_par_rue.items()),
                    columns=["Rue", "Nombre tues pietons"])
            df_result = \
                pd.merge(df_pietons, df_tues_pietons, on="Rue", how="inner")
        
        elif categorie == "cycle":
            df_cyclistes = \
                pd.DataFrame(list(nombre_blesses_cyclistes_par_rue.items()),
                             columns=["Rue", "Nombre blesses cyclistes"])
            df_tues_cyclistes = \
                pd.DataFrame(list(nombre_tues_cyclistes_par_rue.items()),
                             columns=["Rue", "Nombre tues cyclistes"])
            df_result = pd.merge(df_cyclistes, df_tues_cyclistes,
                                 on="Rue", how="inner")
        
        return df_result

    def risque_rue_pieton_velo(data, rue, categorie):
        df_b_m = Utilisateur.df_blesse_mort_rue(data, categorie)
        df_b_m.dropna(subset=["Rue"], inplace=True)
        if rue in df_b_m["Rue"].values:
            df_rue = df_b_m[df_b_m["Rue"].str.contains(rue)]    
            if categorie == "foot":
                nombre_total_pietons_rue_specifique = \
                    df_rue['Nombre blesses pietons'].sum() + df_rue[
                        'Nombre tues pietons'].sum()
                max_injuries_pietons = df_b_m['Nombre blesses pietons'].max()
                max_deaths_pietons = df_b_m['Nombre tues pietons'].max()
                risk_pietons = nombre_total_pietons_rue_specifique / \
                    (max_injuries_pietons + max_deaths_pietons)
                return round(risk_pietons, 3)
            elif categorie == "cycle":
                nombre_total_cyclistes_rue_specifique = \
                    df_rue['Nombre blesses cyclistes'].sum() + df_rue[
                        'Nombre tues cyclistes'].sum()
                max_injuries_cyclistes = df_b_m['Nombre blesses cyclistes'].max()
                max_deaths_cyclistes = df_b_m['Nombre tues cyclistes'].max()
                risk_cyclistes = nombre_total_cyclistes_rue_specifique /\
                    (max_injuries_cyclistes + max_deaths_cyclistes)
                return round(risk_cyclistes, 3)
        else:
            return 0

    def risque_voiture(data, street, voiture):
        nbr_acc = 0
        if voiture == "car" and 'Sedan' in data['VEHICLE.TYPE.CODE.1'].values :         
            if street in data[data["CROSS.STREET.NAME"].str.contains(street) | data["ON.STREET.NAME"].str.contains(street) | data["OFF.STREET.NAME"].str.contains(street)]:
            # Filtrer les données pour la rue spécifique
            # et le type de véhicule spécifique
                test = (data["VEHICLE.TYPE.CODE.1"] == 'Sedan')
                df_filtre_on = data[(data['ON.STREET.NAME'] == rue) & test]
                df_filtre_off = data[(data['OFF.STREET.NAME'] == rue) & test]
                df_filtre_cross = data[(data['CROSS.STREET.NAME'] == rue) & test]
            # Compter le nombre d'accidents après le filtrage
                nbr_acc = len(df_filtre_on) + len(df_filtre_off) + len(df_filtre_cross)
                if nbr_acc == 0:
                    return 0
                if nbr_acc < 5 and nbr_acc > 0:
                    return 0.1
                if nbr_acc < 8 and nbr_acc >= 5:
                    return 0.2
                if nbr_acc < 10 and nbr_acc >= 8:
                    return 0.3
                else:
                    return 0.4
        else:
            return nbr_acc

    def type_vehicule():
        return ['Sedan', 'Station Wagon/Sport Utility Vehicle', 'Taxi', 'Box Truck', 'Ambulance', 'Dump', 'E-Bike', 'Motorcycle', 'Bus', 'FDNY Ambul', 'Pick-up Truck', 'E-Scooter', 'Flat Rack', 'UNK', 'Tractor Truck Diesel', 'Flat Bed', 'GARBAGE TR', 'Bike', 'Garbage or Refuse', 'Van', 'SCHOOL BUS', 'Motorscooter', 'Moped', '3-Door', 'MOPED', 'Chassis Cab', 'Tow Truck / Wrecker', 'Convertible', 'MTA', 'TRAILER', 'AMBULANCE', 'E-bike', 'FIRE TRUCK', 'Refrigerated Van', 'MOTOR SCOO', 'Tractor Truck Gasoline', 'Carry All', 'ambulance', 'Motorbike', 'PICK UP', '4 dr sedan', 'PK', 'Postal ser', 'SANMEN COU']
    
    def risque_rue(data, rue, categorie) : 
        if categorie == 'car' or categorie in Utilisateur.type_vehicule():
            risque = Utilisateur.risque_voiture(data, rue, categorie)
            if risque == None:
                    return 0
            if risque != None:
                return risque*100
        if categorie == "foot" or categorie == "cycle":
            risque = Utilisateur.risque_rue_pieton_velo(data, rue, categorie)
            if risque == None:
                return 0
            if risque != None:
                return risque*100
        else: 
            return 0


data = pd.read_excel("Bronx_sans_Na.xlsx")
te = Utilisateur.risque_rue(data, "BRONXWOOD AVENUE", "foot")
print(te)