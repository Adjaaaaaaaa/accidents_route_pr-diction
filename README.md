# accidents_route_pr-diction

## MCD
```
                 
       |         LIEUX         |                    |   CARACTERISTIQUES    |
       +-----------------------+                    +-----------------------+
       | Num_Acc (PK, FK)      |<-------------------| Num_Acc (PK)          |
       | catr, voie, v1, v2    |      (1,1)         | jour, mois, an, hrmn  |
       | circ, nbv, vosp, prof |      DÉCRIT        | lum, atm, col         |
       | pr, pr1, plan, lartpc |                    | dep, com, agg, int    |
       | larrout, surf, infra  |                    | adr, lat, long        |
       | situ, vma             |                    |                       |
       +-----------------------+                    +-----------------------+
                                                               |
                                                               | (1,n)
                                                               |
                                                          +----V----+
                                                          |IMPLIQUER|
                                                          +----V----+
                                                               |
                                                               | (1,1)
                                                               |
       +-----------------------+                    +----------V------------+
       |        USAGERS        |                    |       VEHICULES       |
       +-----------------------+                    +-----------------------+
       | id_usager (PK)        |      (1,1)         | id_vehicule (PK)      |
       | Num_Acc (FK)          |<-------------------| Num_Acc (FK)          |
       | id_vehicule (FK)      |      OCCUPER /     | num_veh               |
       | num_veh, place, catu  |       HEURTER      | senc, catv, motor     |
       | grav (CIBLE), sexe    |                    | obs, obsm, choc       |
       | an_nais, trajet, secu |      (1,n)         | manv, occutc          |
       | locp, actp, etatp     |                    |                       |
       +-----------------------+                    +-----------------------+
```