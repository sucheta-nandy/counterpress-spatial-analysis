# SSAC27 Research Paper Competition: Abstract (Version A - Methodological Focus)

**Target Competition**: MIT Sloan Sports Analytics Conference 2027 (SSAC27) Research Paper Competition  
**Submission Deadline**: October 1, 2026, 11:59 PM Eastern  
**Framing**: Academic and Methodological  
**Word Count Target**: 420–450 words (Limit: strictly < 500 words including title and headings)  
**Exact Word Count**: **437 words** (including title and headings)

---

### TITLE
When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer

### INTRODUCTION
Counterpressing—applying immediate defensive pressure upon losing possession—is a foundational tactic in modern elite soccer. However, counterpressing represents a high-risk, high-reward tradeoff: committing players forward can pin opponents deep or, if bypassed, expose defensive space that generates high-threat transitions. While existing analyses evaluate counterpressing through aggregate event tags, the spatial configuration present when pressure begins remains poorly understood. We investigate which spatial conditions at counterpress initiation govern two distinct outcomes: regaining possession within 5 seconds and conceding a dangerous transition within 15 seconds.

### METHODS
We analyzed 21,616 distinct open-play counterpress episodes across 414 matches from seven professional competitions in StatsBomb 360 data. Using freeze-frame player coordinates at counterpress initiation, we extracted geometric features capturing local density, player proximity, numerical advantage across concentric rings (5, 10, and 15 StatsBomb coordinate units), and longitudinal/lateral pitch location. Outcomes were strictly defined using event sequences: controlled regain within 5 seconds (34.65% prevalence) and opponent dangerous transition within 15 seconds (22.41% prevalence). We evaluated nested probability models using 5-fold match-clustered cross-validation, paired bootstrap inference, and multivariable clustered logistic regression. Robustness was evaluated across broadcast camera visibility thresholds and leave-one-competition-out partitions.

### RESULTS
Event-level StatsBomb 360 freeze-frame spatial geometry provided modest but statistically reliable incremental predictive value over match context and pitch location alone for 5-second controlled regains (Model 1 Context ROC-AUC = 0.7926 vs Model 3 Full Spatial Logistic ROC-AUC = 0.8156; Delta ROC-AUC = +0.0230, paired bootstrap 95% CI [+0.0181, +0.0278]; Delta PR-AUC = +0.0377). Immediate support was strongly associated with regain odds: holding covariates fixed, shorter nearest-teammate distance was associated with higher regain odds (OR = 0.800 [95% CI: 0.729, 0.878] per 1 SD / 8.2 coordinate units). Local numerical surplus within 10 and 15 units further increased regain odds (OR = 1.071 and 1.144), whereas immediate 5-unit surplus was not independently significant. Conversely, transition danger was dominated by pitch geography: danger rates were nearly three times higher following defensive-third turnovers (31.57%) than attacking-third turnovers (11.28%; OR = 0.379 [95% CI: 0.359, 0.399]). Central counterpresses exhibited higher transition danger than wide counterpresses (25.15% vs 16.86%; OR = 1.219 [95% CI: 1.174, 1.266]). For transition danger, flexible gradient boosting yielded superior probability ranking over linear logistic regression (Delta PR-AUC = +0.0394 [95% CI: +0.0299, +0.0490]).

### CONCLUSION
Counterpress success and counterpress failure risk represent distinct spatial problems. Possession regain is primarily associated with local compactness and immediate teammate proximity around the ball, whereas transition danger is governed by longitudinal depth and pitch centrality. Decision-makers evaluating counterpressing systems should distinguish local ball-recovery conditions from macro-level exposure risk.
