package com.github.davidmoten.geo;

import com.google.common.collect.Sets;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class CoverageLongsTest {
    long[] hashes = {1, 2};
    int count;
    double ratio;
    CoverageLongs coverageLongs;

    @Before
    public void setUp() throws Exception {

        count = 1;
        ratio = 1.1;

        coverageLongs = new CoverageLongs(hashes,count,ratio);
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void getHashes() {
        long[] test = {1};
        assertArrayEquals(test,coverageLongs.getHashes());
    }

    @Test
    public void getRatio() {
        assertEquals(1.1,coverageLongs.getRatio(),0.1);
    }

    @Test
    public void getHashLength() {
        assertEquals(1,coverageLongs.getHashLength());

        long[] hashes = {1, 2};
        int count = 0;
        double ratio = 1.1;
        CoverageLongs coverageCountZero = new CoverageLongs(hashes,count,ratio);
        assertEquals(0,coverageCountZero.getHashLength());

    }

    @Test
    public void getCount() {
        assertEquals(1,coverageLongs.getCount());
    }

//    @Test
//    public void toString1(){
//        long[] hashes = {1, 2};
//        int count = 0;
//        double ratio = 1.1;
//        CoverageLongs coverageCountZero = new CoverageLongs(hashes,count,ratio);
//
//        long[] testHash = coverageCountZero.getHashes();
//        assertEquals("Coverage [hashes=" + testHash + ", ratio=" + ratio + "]",coverageCountZero.toString());
//    }

}