# Define parameters
param (
    [Parameter(Mandatory=$true)]
    [int]$day
)

# Set variables
$dirName = "2024/day$day"
$url = "https://adventofcode.com/2024/day/$day/input"
$cookieFile = "cookie_windows.txt"
$pythonTemplate = @"
class App():
    def __init__(self):
        self.input_data = []
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def solve(self):
        self.read_from_file("input_small.txt")
        #self.read_from_file()
        print(f"{self.input_data=}")       

if __name__ == "__main__":
    App().solve()
"@

# Create the directory
if (-not (Test-Path -Path $dirName)) {
    New-Item -ItemType Directory -Path $dirName | Out-Null
    Write-Host "Directory '$dirName' created successfully."
} else {
    Write-Host "Directory '$dirName' already exists."
}

# Check if session cookie file exists
if (-not (Test-Path -Path $cookieFile)) {
    Write-Host "Session cookie file not found at $cookieFile."
    Write-Host "Please create a file named '.aoc_session' in your home directory with your Advent of Code session cookie."
    exit 1
}

# Fetch the input file
Write-Host "Fetching input file from Advent of Code..."
$sessionCookie = Get-Content $cookieFile -Raw
Invoke-WebRequest -Uri $url -Headers @{ "Cookie" = "session=$sessionCookie" } -OutFile "$dirName\input.txt" -ErrorAction SilentlyContinue
#$response = Invoke-WebRequest -Uri $url -Headers @{ "Cookie" = "session=$sessionCookie" } -OutFile "$dirName\input.txt" -ErrorAction SilentlyContinue

# Check if the fetch was successful
if ($? -and (Test-Path "$dirName\input.txt") -and ((Get-Item "$dirName\input.txt").Length -gt 0)) {
    Write-Host "Input file saved to '$dirName\input.txt'."
} else {
    Write-Host "Failed to fetch the input file. Please check your session cookie and the day number."
    Remove-Item -Path "$dirName\input.txt" -Force -ErrorAction SilentlyContinue
}

# Create part1.py and part2.py with the provided template
Set-Content -Path "$dirName\input_small.txt" -Value ""
Set-Content -Path "$dirName\part1.py" -Value $pythonTemplate
Set-Content -Path "$dirName\part2.py" -Value $pythonTemplate
Write-Host "Files 'part1.py' and 'part2.py' created in '$dirName'."

# Navigate to the directory

Write-Host "Adding files to Git, committing, and pushing..."
& git add "$dirName/input.txt" "$dirName/input_small.txt" "$dirName/part1.py" "$dirName/part2.py"
& git commit -m "Made day $day"
& git push
Write-Host "Git commit and push completed successfully."

Set-Location -Path $dirName