import argparse
from datetime import datetime
from collections import Counter
import csv
def log_mood(name, mood):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = [now, name.lower(), mood.lower()]
    with open("mood_log.csv", "a", newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(entry)
    print("Mood logged.")

def view_log():
    try:
        with open("mood_log.csv", "r") as file:
            print("\nYour Mood Log:\n")
            readable = csv.reader(file)
            for row in readable:
                print(row)
    except FileNotFoundError:
        print("No logs yet.")

def view_stats():
    try:
        with open("mood_log.csv", "r") as file:
            readable = csv.reader(file)
            moods = [row[2] for row in readable]
            mood_counts = Counter(moods)
            for mood, count in mood_counts.items():
                print(f"{mood}: {count}")
    except FileNotFoundError:
        print("No logs yet.")
def filter(name, mood, time):
    inputs = {
    "name": name,
    "mood": mood,
    "time": time
}
    results = []
    try:
        with open("mood_log.csv", "r") as file:
            read = csv.reader(file)
            provided = {key: val for key, val in inputs.items() if val}
            if time:
                time = time.strftime("%Y-%m-%d")
            for row in read:
                if time == row[0] and mood == row[2] and name == row[1]:
                    results.append(row)
                elif len(provided) == 2:
                    if name == row[1] and mood == row[2]:
                        results.append(row)
                    elif name == row[1] and time == row[0].split(" ")[-1]:
                        results.append(row)
                    elif mood == row[2] and time == row[0].split(" ")[-1]:
                        results.append(row)
                    else:
                        None
                else:
                    if time == row[0].split(" ")[-1] or name == row[1] or mood == row[2]:
                        results.append(row)
            if results:
                print("Here are the results:\n")
                for row in results:
                    print(", ".join(row))
                
            else:
                print("No matching entries found.")

    except FileNotFoundError:
        print("No logs yet.")

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
         raise argparse.ArgumentTypeError(f"Not a valid date: {s} use only %YYYY-%mm-%dd")            
        
def main():
    parser = argparse.ArgumentParser(description="Mood Logger CLI")
    parser.add_argument("--name", type=str, help="Your name")
    parser.add_argument("--mood", type=str, help="Your current mood")
    parser.add_argument("--view", action="store_true", help="View mood log")
    parser.add_argument("--stats", action="store_true", help="Shows logs stats")
    parser.add_argument("--filter", action="store_true", help="filter accroding to --name and --mood")
    parser.add_argument("--date", type=valid_date, help="Filter by date (YYYY-MM-DD)")
    
    args = parser.parse_args()

    if args.view:
        view_log()
    elif args.stats:
        view_stats()
    elif args.filter and (args.mood or args.name or args.date):
        filter(args.name or None, args.mood or None, args.date or None)
    elif args.name and args.mood:
        log_mood(args.name, args.mood)
    elif args.name or args.mood:
        print("You must provide both --name and --mood to log an entry. Or use --filter to search.")
    else:
        print("Use --name and --mood to log, or --view to read logs.")
if __name__ == "__main__":
    main()
    