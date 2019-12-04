function Is-Numeric ($Value) {
    return $Value -match "^[\d\.]+$"
    }

# Fantasy Data Reporting
$data = import-csv "C:\Users\student\Downloads\ffdata.csv"

# Formatting all numeric fields as doubles for proper sorting
$props = ($data | gm | ? membertype -eq noteproperty).Name
foreach ($prop in $props){
    if (Is-Numeric $data.$prop){
        $data | % {$_.$prop = [double]$_.$prop}
        }
    }

# Getting unique list of teams for iteration
$teams = $data.team | sort -Unique

# Get best RB Matchups based on rush yard upside, receiving yard upside, TD upside (rushing and receiving)
$allowdata = @()

foreach ($team in $teams){
    # RBStuff
    $rb20plus = @($data | ? position -eq RB | ? opponent -eq $team | ? FantasyPointsPPR -ge 20) 
    $rb100ruyds = @($data | ? position -eq RB | ? opponent -eq $team | ? rushingyards -ge 100)
    $rb100recyds = @($data | ? position -eq RB | ? opponent -eq $team | ? receivingyards -ge 100)
    $rb7recs = @($data | ? position -eq RB | ? opponent -eq $team | ? receptions -ge 7)
    $rbruTDs = @($data | ? position -eq RB | ? opponent -eq $team | ? RushingTouchdowns -ge 1)
    $rbrecTDs = @($data | ? position -eq RB | ? opponent -eq $team | ? ReceivingTouchdowns -ge 1)
    
    # WR stuff
    $wr20plus = @($data | ? position -eq WR | ? opponent -eq $team | ? FantasyPointsPPR -ge 20) 
    $wr100recyds = @($data | ? position -eq WR | ? opponent -eq $team | ? receivingyards -ge 100)
    $wr7recs = @($data | ? position -eq WR | ? opponent -eq $team | ? receptions -ge 7)
    $wrrecTDs = @($data | ? position -eq WR | ? opponent -eq $team | ? ReceivingTouchdowns -ge 1)

    # TE stuff
    $te15plus = @($data | ? position -eq TE | ? opponent -eq $team | ? FantasyPointsPPR -ge 15) 
    $te100recyds = @($data | ? position -eq TE | ? opponent -eq $team | ? receivingyards -ge 100)
    $te5recs = @($data | ? position -eq TE | ? opponent -eq $team | ? receptions -ge 5)
    $terecTDs = @($data | ? position -eq TE | ? opponent -eq $team | ? ReceivingTouchdowns -ge 1)

    # QB stuff
    $qb25plus = @($data | ? position -eq qb | ? opponent -eq $team | ? FantasyPointsPPR -ge 25) 
    $qb300recyds = @($data | ? position -eq qb | ? opponent -eq $team | ? passingyards -ge 300)
    $qb2TDs = @($data | ? position -eq qb | ? opponent -eq $team | ? passingtouchdowns -ge 5)

    # Writing rows

    $orow = new-object psobject
    $orow | Add-Member -MemberType NoteProperty -Name 'Team' -Value $team
    $orow | Add-Member -MemberType NoteProperty -Name 'RB20Plus' -Value $rb20plus.count
    $orow | Add-Member -MemberType NoteProperty -Name 'RB100yds' -Value $rb100ruyds.count
    $orow | Add-Member -MemberType NoteProperty -Name 'RB100recyds' -Value $rb100recyds.count
    $orow | Add-Member -MemberType NoteProperty -Name 'RBRecs7' -Value $rb7recs.count
    $orow | Add-Member -MemberType NoteProperty -Name 'RBRuTD' -Value $rbruTDs.count
    $orow | Add-Member -MemberType NoteProperty -Name 'RBRecTDs' -Value $rbrecTDs.count
    $orow | Add-Member -MemberType NoteProperty -Name 'WR20plus' -Value $wr20plus.count
    $orow | Add-Member -MemberType NoteProperty -Name 'WRRecYds' -Value $wr100recyds.count
    $orow | Add-Member -MemberType NoteProperty -Name 'WR7Recs' -Value $wr7recs.count
    $orow | Add-Member -MemberType NoteProperty -Name 'WRRecTDs' -Value $wrrecTDs.count
    $orow | Add-Member -MemberType NoteProperty -Name 'TE15plus' -Value $te15plus.count
    $orow | Add-Member -MemberType NoteProperty -Name 'TE100RecYds' -Value $te100recyds.count
    $orow | Add-Member -MemberType NoteProperty -Name 'TE5Recs' -Value $te5recs.count
    $orow | Add-Member -MemberType NoteProperty -Name 'TERecTDs' -Value $terecTDs.count
    $orow | Add-Member -MemberType NoteProperty -Name 'QB25Plus' -Value $qb25plus.count
    $orow | Add-Member -MemberType NoteProperty -Name 'QB300PassYds' -Value $qb300recyds.count
    $orow | Add-Member -MemberType NoteProperty -Name 'QB2PlusTDs' -Value $qb2TDs.count

    $allowdata += $orow
    }


# Setting tops for each category for report building
$rb20 = $allowdata | ? RB20Plus  -gt 0| sort RB20Plus -desc | select team,RB20Plus,RB100yds,RB100recyds,RBRecs7,RBRuTD,RBRecTDs -first 7
$rb100 = $allowdata | ? RB100yds  -gt 0| sort RB100yds -desc | select team,RB20Plus,RB100yds,RB100recyds,RBRecs7,RBRuTD,RBRecTDs -first 7
$rb100rec = $allowdata | ? RB100recyds  -gt 0| sort RB100recyds -desc | select team,RB20Plus,RB100yds,RB100recyds,RBRecs7,RBRuTD,RBRecTDs -first 7
$rb7rec = $allowdata | ? RBRecs7  -gt 0| sort RBRecs7 -desc | select team,RB20Plus,RB100yds,RB100recyds,RBRecs7,RBRuTD,RBRecTDs -first 7
$rbruTD = $allowdata | ? RBRuTD  -gt 0| sort RBRuTD -desc | select team,RB20Plus,RB100yds,RB100recyds,RBRecs7,RBRuTD,RBRecTDs -first 7
$rbrecTD = $allowdata | ? RBRecTDs  -gt 0| sort RBRecTDs -desc | select team,RB20Plus,RB100yds,RB100recyds,RBRecs7,RBRuTD,RBRecTDs -first 7
$wr20 = $allowdata | ? WR20plus  -gt 0| sort WR20plus -desc | select team,WR20plus, WR7Recs, WRRecTDs, WRRecYds -first 7
$wr7rec = $allowdata | ? WR7Recs  -gt 0| sort WR7Recs -desc | select team,WR20plus, WR7Recs, WRRecTDs, WRRecYds -first 7
$wrTD = $allowdata | ? WRRecTDs  -gt 0| sort WRRecTDs -desc | select team,WR20plus, WR7Recs, WRRecTDs, WRRecYds -first 7
$wryds = $allowdata | ? WRRecYds  -gt 0| sort WRRecYds -desc | select team,WR20plus, WR7Recs, WRRecTDs, WRRecYds -first 7
$te15 = $allowdata | ? TE15plus  -gt 0| sort TE15plus -desc | select team,TE15plus, TE5Recs, TERecTDs, TE100RecYds -first 7
$te5rec = $allowdata | ? TE5Recs  -gt 0| sort TE5Recs -desc | select team,TE15plus, TE5Recs, TERecTDs, TE100RecYds -first 7
$teTD = $allowdata | ? TERecTDs  -gt 0| sort TERecTDs -desc | select team,TE15plus, TE5Recs, TERecTDs, TE100RecYds -first 7
$teyds = $allowdata | ? TERecYds  -gt 0| sort TERecYds -desc | select team,TE15plus, TE5Recs, TERecTDs, TE100RecYds -first 7
$qb25 = $allowdata | ? QB25Plus  -gt 0| sort QB25Plus -desc |select team,QB25Plus, QB2PlusTDs, QB300PassYds -first 7
$qbTD = $allowdata | ? QB2PlusTDs  -gt 0| sort QB2PlusTDs -desc |select team,QB25Plus, QB2PlusTDs, QB300PassYds -first 7
$qb300 = $allowdata | ? QB300PassYds  -gt 0| sort QB300PassYds -desc |select team,QB25Plus, QB2PlusTDs, QB300PassYds -first 7

$report = @()
# TOP Matchups
foreach ($team in $teams){
    $report += "Stats of fantasy performance allowed by $team"
    if ($team -in $rb20.team){$report += "$team is top 7 in number of 20+ point performances to RBs."}
    if ($team -in $rb100.team){$report += "$team is top 7 in number of 100 rushing yard performances to RBs."}
    if ($team -in $rb100rec.team){$report += "$team is top 7 in number of 100 receiving yard performances to RBs."}
    if ($team -in $rb7rec.team){$report += "$team is top 7 in number of 7+ reception performances to RBs."}
    if ($team -in $rbrutd.team){$report += "$team is top 7 in number of games/player allowing a rushing TD to a running back."}
    if ($team -in $rbrectd.team){$report += "$team is top 7 in number of games/player allowing a receiving TD to a running back."}
    if ($team -in $wr20.team){$report += "$team is top 7 in number of 20+ point performances to WRs."}
    if ($team -in $wr7rec.team){$report += "$team is top 7 in number of 7+ reception performances to WRs."}
    if ($team -in $wrTD.team){$report += "$team is top 7 in number of games/player allowing a receiving TD to a wide receiver."}
    if ($team -in $wryds.team){$report += "$team is top 7 in number of 100 receiving yard performances to WRs."}
    if ($team -in $te15.team){$report += "$team is top 7 in number of 15+ point performances to TEs."}
    if ($team -in $te5rec.team){$report += "$team is top 7 in number of 7+ reception performances to TEs."}
    if ($team -in $teTD.team){$report += "$team is top 7 in number of games/player allowing a receiving TD to a TE."}
    if ($team -in $teyds.team){$report += "$team is top 7 in number of 100 receiving yard performances to TEs."}
    if ($team -in $qb25.team){$report += "$team is top 7 in number of 25+ point performances to QBs."}
    if ($team -in $QBtd.team){$report += "$team is top 7 in number of multi TD performances to QBs."}
    if ($team -in $qb300.team){$report += "$team is top 7 in number of 300+ passing yard games to a QB."}
    $report += "******************************************************`n`n"
    }
