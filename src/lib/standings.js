export function calculateStandings(matches, teamNames) {
  // Initialize teams
  const stats = {}
  teamNames.forEach(name => {
    stats[name] = {
      name,
      p: 0,
      w: 0,
      d: 0,
      l: 0,
      gf: 0,
      ga: 0,
      gd: 0,
      pts: 0
    }
  })

  // Process matches
  matches.forEach(match => {
    if (!match.is_played) return
    
    const t1 = match.team1
    const t2 = match.team2
    const s1 = match.score1 || 0
    const s2 = match.score2 || 0

    // Ensure teams exist in stats
    if (!stats[t1]) stats[t1] = { name: t1, p:0, w:0, d:0, l:0, gf:0, ga:0, gd:0, pts:0 }
    if (!stats[t2]) stats[t2] = { name: t2, p:0, w:0, d:0, l:0, gf:0, ga:0, gd:0, pts:0 }

    stats[t1].p += 1
    stats[t2].p += 1

    stats[t1].gf += s1
    stats[t1].ga += s2

    stats[t2].gf += s2
    stats[t2].ga += s1

    if (s1 > s2) {
      stats[t1].w += 1
      stats[t2].l += 1
      stats[t1].pts += 3
      stats[t2].pts += 1
    } else if (s1 < s2) {
      stats[t2].w += 1
      stats[t1].l += 1
      stats[t2].pts += 3
      stats[t1].pts += 1
    } else {
      stats[t1].d += 1
      stats[t2].d += 1
      stats[t1].pts += 2
      stats[t2].pts += 2
    }
  })

  // Calculate GD and map to array
  const standings = Object.values(stats).map(team => {
    team.gd = team.gf - team.ga
    return team
  })

  // Sort by PTS > GD > GF
  standings.sort((a, b) => {
    if (b.pts !== a.pts) return b.pts - a.pts
    if (b.gd !== a.gd) return b.gd - a.gd
    return b.gf - a.gf
  })

  return standings
}
