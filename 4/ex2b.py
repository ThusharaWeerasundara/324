import ex2a #import ex2a for use the method github_superstars

repos_with_most_stars = ex2a.github_superstars("cepdnaclk")  #get repos with post stars
print("Wining repo: " + repos_with_most_stars[0][1] + ", by: " + repos_with_most_stars[0][0] + ", with: " + str(repos_with_most_stars[0][2]) + " stars")
