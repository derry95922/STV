package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.*;

public class CoverageTest {

    Coverage coverage;
    Set<String> hashes;
    @Before
    public void setUp() throws Exception {
        hashes = new HashSet<String>();
        hashes.add("abc");
        double ratio = 0;
        coverage = new Coverage(hashes, ratio);
    }
    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void getHashes() {
        assertEquals(hashes,coverage.getHashes());
    }

    @Test
    public void getRatio() {
        assertEquals(0,coverage.getRatio(),0.1);
    }

    @Test
    public void getHashLength() {
        assertEquals(3,coverage.getHashLength());
    }

    @Test
    public void toStringText() {
        assertEquals("Coverage [hashes=[abc], ratio=0.0]",coverage.toString());
    }
}