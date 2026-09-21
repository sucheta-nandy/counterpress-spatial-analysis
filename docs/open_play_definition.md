# Methodological Definition: Open-Play vs. Set-Piece Restart Turnovers

## 1. Tactical & Methodological Motivation

In StatsBomb event data, every possession chain is tagged with a `play_pattern` representing how the possession originated (e.g. `Regular Play`, `From Counter`, `From Throw In`, `From Free Kick`, `From Corner`, `From Goal Kick`).

In initial extraction (Iteration 2), all possessions originating from set pieces were categorically excluded from the open-play cohort (4,831 episodes). However, an empirical audit revealed that:
1. **Possession origin does NOT equate to turnover context**: Over 70% of possessions originating from a throw-in or free kick completed 3 to 8 passes and lasted 10 to 25 seconds before turning the ball over.
2. When a team establishes multi-pass circulation following a throw-in or goal kick, outfield players transition into standard attacking shapes, and the defending team organizes into its defensive structure. When the ball is subsequently turned over, the counterpressing situation is a **genuine open-play transition**, governed by open-play spatial geometry rather than set-piece box packing.
3. Conversely, when the turnover occurs immediately on the delivery of a corner or throw-in (e.g. contested header or direct interception), players remain locked in set-piece marking assignments.

---

## 2. The Reproducible 3-Way Classification Rule

We formalize two distinct attributes for every counterpress episode:
- **`possession_origin_pattern`**: The raw StatsBomb `play_pattern` of the possession chain.
- **`turnover_context`**: The tactical state of the turnover event itself, partitioned into:
  * `open_play`
  * `immediate_restart_phase`
  * `ambiguous`

### Algorithmic Decision Logic:
```python
def classify_turnover_context(origin_pattern, elapsed_seconds, successful_passes, is_restart_event=False):
    # 1. Native Open-Play Origins
    if origin_pattern in {'Regular Play', 'From Counter', 'From Keeper'}:
        return 'open_play'

    # 2. Immediate Restart Phase
    # Turnover occurred on the restart action itself, or with 0 completed passes, or in < 3.0 seconds
    if is_restart_event or successful_passes == 0 or elapsed_seconds < 3.0:
        return 'immediate_restart_phase'

    # 3. Established Open Play from Restart
    # Team completed >= 2 successful passes AND possessed ball for >= 5.0 seconds
    elif successful_passes >= 2 and elapsed_seconds >= 5.0:
        return 'open_play'

    # 4. Ambiguous Transition Zone
    # (e.g. exactly 1 completed pass, or 3.0s <= elapsed < 5.0s)
    else:
        return 'ambiguous'
```

---

## 3. Cohort Eligibility Impact

Only episodes where:
```python
turnover_context == "open_play"
```
are eligible for the primary modeling cohort. This retains genuine open-play counterpresses that developed from restarts while rigorously filtering out set-piece deliveries and chaotic restart scrambles.
