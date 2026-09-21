# SSAC27 Research Paper Competition: Abstract (Version B - Practitioner Focus)

**Target Competition**: MIT Sloan Sports Analytics Conference 2027 (SSAC27) Research Paper Competition  
**Submission Deadline**: October 1, 2026, 11:59 PM Eastern  
**Framing**: Practitioner and Tactical Decision-Making Focus  
**Word Count Target**: 420–450 words (Limit: strictly < 500 words including title and headings)  
**Exact Word Count**: **439 words** (including title and headings)

---

### TITLE
When Does the Counterpress Work? Spatial Predictors of Possession Regain and Transition Risk in Elite Soccer

### INTRODUCTION
Modern soccer tactics emphasize counterpressing to disrupt opponent counterattacks and sustain attacking momentum. Yet aggressive pressing immediately after losing possession carries tactical hazard: overcommitting players can strand defenders ahead of the ball, exposing central space to opponent transition attacks. While analysts frequently tally counterpress volumes, teams lack objective spatial criteria to evaluate when a counterpress should be triggered versus when defenders should drop and delay. Using event-level freeze frames, we examine the spatial conditions that govern whether an immediate counterpress achieves a controlled possession regain within 5 seconds or concedes a dangerous opponent transition within 15 seconds.

### METHODS
We analyzed 21,616 distinct open-play counterpress episodes across 414 matches from seven professional competitions using StatsBomb 360 data. From freeze frames captured at counterpress initiation, we quantified local player density, teammate proximity, numerical advantage across concentric rings (5, 10, and 15 StatsBomb coordinate units), and pitch location. Using chronological event sequences, we tracked 5-second controlled regains (34.65% baseline prevalence) and 15-second dangerous opponent transitions (22.41% baseline prevalence). We evaluated nested probability models via 5-fold match-clustered cross-validation, paired bootstrap inference, and multivariable clustered logistic regression, auditing robustness across camera visibility thresholds and competition holdouts.

### RESULTS
StatsBomb 360 freeze-frame spatial geometry provided modest but statistically reliable incremental predictive value over match context and pitch location for 5-second regains (Model 1 Context ROC-AUC = 0.7926 vs Model 3 Full Spatial Logistic ROC-AUC = 0.8156; Delta ROC-AUC = +0.0230, paired bootstrap 95% CI [+0.0181, +0.0278]; Delta PR-AUC = +0.0377). Immediate support dictated regain odds: holding covariates fixed, shorter nearest-teammate distance was strongly associated with higher regain odds (OR = 0.800 [95% CI: 0.729, 0.878] per 1 SD / 8.2 coordinate units). Local numerical surplus at 10 and 15 units further increased regain odds (OR = 1.071 and 1.144), while an immediate 5-unit surplus was not independently significant. Conversely, transition danger was dominated by pitch geography: danger rates were nearly three times higher following defensive-third turnovers (31.57%) than attacking-third turnovers (11.28%; OR = 0.379 [95% CI: 0.359, 0.399]). Central counterpresses exhibited substantially greater transition danger than wide counterpresses (25.15% vs 16.86%; OR = 1.219 [95% CI: 1.174, 1.266]), with non-linear models yielding superior danger ranking (Delta PR-AUC = +0.0394 [95% CI: +0.0299, +0.0490]).

### CONCLUSION
Counterpressing effectiveness involves two independent tactical realities. Winning the ball back quickly depends on local compactness and immediate teammate proximity around the turnover, whereas conceding transition danger is governed by pitch depth and centrality. Tactical systems must separate pressing cues from exposure risks, recognizing that central counterpresses without immediate compact support carry disproportionate downside.
