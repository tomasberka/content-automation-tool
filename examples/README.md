# HelloComp Dashboard - Examples

This directory contains example scripts for using the HelloComp Dashboard and Analytics Manager.

## Available Examples

### 1. add_daily_metrics.py
**Purpose:** Manually add daily metrics to the dashboard

**Usage:**
```bash
# Add today's metrics
python examples/add_daily_metrics.py

# Add a week of sample metrics
python examples/add_daily_metrics.py --weekly
```

**What it does:**
- Adds sample metrics for website, Facebook, and Instagram
- Generates a daily/weekly report
- Exports data to JSON backup file

**When to use:**
- When you don't have API integration set up yet
- For testing the dashboard functionality
- For manually tracking metrics from various sources

---

### 2. compare_periods.py
**Purpose:** Compare metrics between two time periods

**Usage:**
```bash
# Compare this week vs last week
python examples/compare_periods.py --week

# Compare this month vs last month
python examples/compare_periods.py --month

# Custom comparison (provide 4 dates: period1_start, period1_end, period2_start, period2_end)
python examples/compare_periods.py 2026-01-01 2026-01-31 2026-02-01 2026-02-28
```

**What it does:**
- Loads historical metrics from backup file
- Compares metrics between two periods
- Shows percentage changes with indicators (📈 📉 ➡️)
- Helps identify trends and performance changes

**When to use:**
- During weekly/monthly reviews
- To track performance trends
- To evaluate the impact of changes

---

## Quick Start

### 1. Run the basic example
```bash
cd /home/runner/work/content-automation-tool/content-automation-tool
python examples/add_daily_metrics.py
```

This will:
1. Create sample metrics for today
2. Generate a daily report
3. Save data to `metrics_backup_YYYY-MM-DD.json`

### 2. Add a week of data
```bash
python examples/add_daily_metrics.py --weekly
```

### 3. Compare periods
```bash
python examples/compare_periods.py --week
```

---

## Creating Your Own Examples

You can create your own scripts based on these examples:

```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hellcomp_dashboard import HelloCompDashboard
from analytics_manager import AnalyticsManager, Platform, MetricType

# Initialize
dashboard = HelloCompDashboard()

# Add metrics
dashboard.add_manual_metric('website', 'visitors', 1250)
dashboard.add_manual_metric('facebook', 'engagement', 4.2)

# Generate report
report = dashboard.generate_daily_report()
print(report)
```

---

## Tips

1. **Backup your data regularly:**
   ```python
   manager.export_to_json('metrics_backup.json')
   ```

2. **Load historical data:**
   ```python
   manager.import_from_json('metrics_backup.json')
   ```

3. **Use consistent filenames** for backups to make comparisons easier

4. **Set up a cron job** to run scripts automatically:
   ```bash
   # Daily at 9 AM
   0 9 * * * cd /path/to/project && python examples/add_daily_metrics.py
   ```

---

## Further Reading

- **Main Dashboard Documentation:** [../HELLCOMP-DASHBOARD.md](../HELLCOMP-DASHBOARD.md)
- **Quick Start Guide:** [../DASHBOARD-QUICKSTART.md](../DASHBOARD-QUICKSTART.md)
- **API Reference:** See docstrings in `analytics_manager.py` and `hellcomp_dashboard.py`
