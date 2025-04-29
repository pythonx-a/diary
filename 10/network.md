# Cahier des Charges – Projet Python : Scanner et Mappage Réseau Intelligent

## 1. Objectif du projet

Développer un outil Python permettant de :
- Scanner un réseau local (ou simulé)
- Identifier automatiquement les hôtes (PC, routeurs, VMs, etc.)
- Collecter des informations via ARP, Ping, Nmap et SNMP
- Déterminer les connexions logiques entre les hôtes
- Générer dynamiquement une **topologie** du réseau
- Fournir une interface (CLI ou Web) pour interagir avec les résultats

---

## 2. Fonctionnalités

| Module                   | Description |
|--------------------------|-------------|
|  Scan réseau           | Scan IP/ARP pour détecter les hôtes actifs |
|  Découverte SNMP       | Récupération d’infos sur les hôtes via SNMP (si dispo) |
|  Analyse de topologie  | Construction d’un graphe logique des connexions |
|  Visualisation         | Affichage interactif ou statique de la topologie réseau |
|  Export & sauvegarde   | Export des résultats en JSON, PDF, ou image |
|  Interface utilisateur | CLI ou interface Web (Streamlit/Dash) |

---

## 3. Technologies

- **Langage principal** : Python 3.10+
- **Scan & collecte** :
  - [`scapy`](https://scapy.net/) – manipulation de paquets réseau
  - [`nmap`](https://nmap.org/) + `python-nmap` – scan des ports/hôtes
  - [`pysnmp`](https://pysnmp.readthedocs.io/) – SNMP
- **Analyse / graphe** :
  - `networkx`, `ipaddress`
- **Visualisation** :
  - `Graphviz`, `pygraphviz`, `plotly`, `matplotlib`, `streamlit`
- **Interface** :
  - `argparse` pour la CLI
  - `streamlit` ou `dash` pour interface Web
- **Tests / qualité** :
  - `pytest`, `flake8`, `black`

---

## 4. Répartition des tâches – Équipe de 4 personnes

| Membre      | Responsabilités principales      | Tâches spécifiques (en collaboration) |
|-------------|----------------------------------|----------------------------------------|
| Personne A  | Scan & Collecte des données      | - Implémenter le scan ARP et Ping<br>- Intégration de `scapy` et `python-nmap`<br>- Préparer les structures de données partagées |
| Personne B  | Découverte SNMP + Orchestration  | - Intégrer SNMP avec `pysnmp`<br>- Gérer les cas de timeout / non-réponse<br>- Ébaucher la CLI (avec `argparse`) pour piloter les modules |
| Personne C  | Analyse de topologie             | - Analyser les données collectées<br>- Construire le graphe réseau avec `networkx`<br>- Déterminer les connexions logiques entre hôtes |
| Personne D  | Visualisation & Export           | - Affichage de la topologie avec `pygraphviz`, `plotly`, etc.<br>- Interface utilisateur (Streamlit ou Dash)<br>- Export JSON / image / PDF |
